from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel
import torch
from pathlib import Path

# Paths
base_model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
lora_model_path = Path("C:/Users/affu4/OneDrive/Desktop/Task/lora_adapter")

# Load model + tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
base_model = AutoModelForCausalLM.from_pretrained(base_model_name)
model = PeftModel.from_pretrained(base_model, lora_model_path)

# Text generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

# Prompt
question = "Execute a Git subcommand:"
prompt = f"Q: {question}\nA:"

# Generate
output = pipe(prompt, max_new_tokens=50, do_sample=False)[0]["generated_text"]

# Display result
print("🔍 Prompt:\n", prompt)
print("\n🧠 Model Output:\n",output)