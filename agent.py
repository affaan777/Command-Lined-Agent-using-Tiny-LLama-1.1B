# ===============================
# 🤖 agent.py — CLI Agent for TinyLlama LoRA
# Usage: python agent.py "your command-line query" or run interactively
# ===============================

import sys
import json
import torch
from datetime import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import os
from pathlib import Path

# Load paths
base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
adapter_dir = "lora_adapter"  # Fine-tuned LoRA weights
log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / "trace.jsonl"

# ✅ Load model and tokenizer once
print("🔄 Loading TinyLlama base model + LoRA adapter...")
tokenizer = AutoTokenizer.from_pretrained(adapter_dir)
base = AutoModelForCausalLM.from_pretrained(base_model)
model = PeftModel.from_pretrained(base, adapter_dir)
model.eval()

# ✅ Inference function
def generate_answer(query):
    prompt = f"Q: {query}\nA:"
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # ✅ Log the result
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "response": response
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    return response

# ✅ Support both modes
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Single query from command line
        query = sys.argv[1].strip()
        response = generate_answer(query)
        print("\n🧠 Model Response:\n")
        print(response)
        print(f"\n✅ Logged to {log_path}")
    else:
        # Interactive mode
        print("\n🤖 CLI AGENT READY – Type 'exit' to quit.\n")
        while True:
            query = input("Q: ")
            if query.strip().lower() in ["exit", "quit"]:
                break
            response = generate_answer(query)
            print(f"A: {response}\n")
