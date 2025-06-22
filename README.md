This project demonstrates the complete pipeline for fine-tuning a TinyLlama model using LoRA on a curated dataset of 150+ CLI-related Q&A pairs, and wrapping it into a CLI agent interface for real-world command-line assistance.

⚙️ Setup Instructions

1. 🔁 Clone Repo & Create Environment

git clone <your-private-repo-link>
cd <project-folder>
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

2. 📦 Install Requirements

pip install -r requirements.txt

If `requirements.txt` is missing, install manually:

pip install torch transformers datasets peft rouge-score accelerate

🧠 Run CLI Agent

▶️ Fine-Tuned Model (agent.py)

python agent.py "Create a new Git branch and switch to it"

▶️ Base Model (base_agent.py)

python base_agent.py "Create a new Git branch and switch to it"

Logs will be saved automatically to `logs/trace.jsonl`

📚 Train the Model (LoRA + CPU)

Run your training script (e.g., `train.py` or `model.py`):

python model.py

This will:

- Load `cli_qa_dataset.json`
- Fine-tune `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- Save the adapter to `lora_adapter/`

📊 Evaluate

1. Static Evaluation (Base vs Fine-Tuned)
   Edit and review `eval_static.md`

2. Dynamic Evaluation (CLI Agent)
   Run 7 test queries → `logs/trace.jsonl` → summarize in `eval_dynamic.md`

3. ROUGE-L Metric
   python eval_metrics.py
