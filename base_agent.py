import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load base model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
print("🔄 Loading base model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

# Inference function
def generate_base_answer(question):
    prompt = f"Q: {question}\nA:"
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Interactive CLI loop
if __name__ == "__main__":
    print("\n🧠 Base Model Ready – Ask your CLI questions (type 'exit' to quit)\n")
    while True:
        query = input("Q: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = generate_base_answer(query)
        print(f"A: {answer}\n")
