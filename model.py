import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
from datasets import Dataset
import json
import gc
import os
from typing import Dict, List
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def verify_dependencies():
    """Verify all required packages are installed."""
    required_packages = ['torch', 'transformers', 'datasets', 'peft', 'trl', 'accelerate']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        logger.error(f"Missing required packages: {', '.join(missing_packages)}")
        logger.info("Please install them using: pip install -r requirements.txt")
        sys.exit(1)

def load_model_and_tokenizer(model_name: str) -> tuple:
    """Load model and tokenizer with error handling."""
    try:
        logger.info("Loading model on CPU...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise

def load_and_preprocess_data(file_path: str, max_samples: int = 150) -> Dataset:
    """Load and preprocess dataset with error handling."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset file not found: {file_path}")

        logger.info("Loading and tokenizing dataset...")
        with open(file_path, "r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Dataset must be a list of dictionaries")

        # Validate data format
        for item in data:
            if not isinstance(item, dict) or 'question' not in item or 'answer' not in item:
                raise ValueError("Each item in dataset must be a dictionary with 'question' and 'answer' keys")

        # Clean and shorten Q&A for faster training
        formatted_data = [
            {"text": f"Q: {item['question'].strip()}\nA: {item['answer'].strip()}"}
            for item in data
            if len(item['question']) < 200 and len(item['answer']) < 300
        ][:max_samples]

        if not formatted_data:
            raise ValueError("No valid data samples found after filtering")

        logger.info(f"Loaded {len(formatted_data)} samples")
        return Dataset.from_list(formatted_data)
    except Exception as e:
        logger.error(f"Error loading dataset: {str(e)}")
        raise

def main():
    # Verify dependencies first
    verify_dependencies()

    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    output_dir = "./tinyllama_lora_cpu_output"
    adapter_dir = "./lora_adapter"
    dataset_path = "cli_qa_dataset.json"

    try:
        # Create output directories if they don't exist
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(adapter_dir, exist_ok=True)

        # Load model and tokenizer
        model, tokenizer = load_model_and_tokenizer(model_name)

        # Apply LoRA configuration
        lora_config = LoraConfig(
            r=8,
            lora_alpha=16,
            target_modules=["q_proj", "v_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        model = get_peft_model(model, lora_config)

        # Load and preprocess dataset
        dataset = load_and_preprocess_data(dataset_path)

        # Split dataset into train and validation
        dataset = dataset.train_test_split(test_size=0.1, seed=42)
        train_dataset = dataset["train"]
        val_dataset = dataset["test"]

        def tokenize_function(example):
            return tokenizer(
                example["text"],
                truncation=True,
                padding="max_length",
                max_length=256
            )

        # Tokenize datasets
        tokenized_train = train_dataset.map(tokenize_function, batched=True)
        tokenized_val = val_dataset.map(tokenize_function, batched=True)

        # Training Setup
        from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling

        training_args = TrainingArguments(
           output_dir=output_dir,
           per_device_train_batch_size=2,
           per_device_eval_batch_size=2,
           num_train_epochs=1,
           learning_rate=2e-4,
           logging_steps=10
        )
           

        data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_train,
            eval_dataset=tokenized_val,
            tokenizer=tokenizer,
            data_collator=data_collator
        )

        # Train
        logger.info("Starting training...")
        trainer.train()

        # Save Adapter
        model.save_pretrained(adapter_dir)
        tokenizer.save_pretrained(adapter_dir)
        logger.info(f"✅ LoRA adapter saved in {adapter_dir}")

        # Clean up memory
        del model
        del trainer
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None

    except Exception as e:
        logger.error(f"An error occurred during training: {str(e)}")
        raise

if __name__ == "__main__":
    main()
