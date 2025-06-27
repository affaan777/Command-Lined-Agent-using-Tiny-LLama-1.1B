# 📦 AI/ML Internship Task – TinyLlama CLI Agent

This project demonstrates the complete pipeline for fine-tuning a TinyLlama model using LoRA on a curated dataset of 150+ CLI-related Q\&A pairs, and wrapping it into a CLI agent interface for real-world command-line assistance.

---

## ✅ Project Structure

```
├── agent.py               # CLI agent using fine-tuned LoRA adapter
├── base_agent.py          # Baseline agent using original TinyLlama
├── cli_qa_dataset.json    # Curated dataset of 150+ command-line Q&A pairs
├── logs/                  # Logs of agent interactions
│   └── trace.jsonl
├── lora_adapter/          # Output directory for saved LoRA adapter weights
├── tinyllama_lora_cpu_output/ # Training outputs
├── eval_static.md         # Static evaluation report (Base vs Finetuned)
├── eval_dynamic.md        # Real-time evaluation from agent runs
├── report.md              # One-page summary of data, training, results
├── eval_metrics.py        # Computes ROUGE-L scores for static evaluation
└── README.md              # (You are here)
```

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone Repo & Create Environment

```bash
git clone <your-private-repo-link>
cd <project-folder>
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install torch transformers datasets peft rouge-score accelerate
```

---

## 🧠 Run CLI Agent

### ▶️ Fine-Tuned Model (agent.py)

```bash
python agent.py "Create a new Git branch and switch to it"
```

### ▶️ Base Model (base\_agent.py)

```bash
python base_agent.py "Create a new Git branch and switch to it"
```

Logs will be saved automatically to `logs/trace.jsonl`

---

## 📚 Train the Model (LoRA + CPU)

### Run your training script (e.g., `train.py` or `model.py`):

```bash
python model.py
```

This will:

* Load `cli_qa_dataset.json`
* Fine-tune `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
* Save the adapter to `lora_adapter/`

---

## 📊 Evaluate

### 1. Static Evaluation (Base vs Fine-Tuned)

Edit and review `eval_static.md`

### 2. Dynamic Evaluation (CLI Agent)

Run 7 test queries → `logs/trace.jsonl` → summarize in `eval_dynamic.md`

### 3. ROUGE-L Metric

```bash
python eval_metrics.py
```

---

## 📝 Submission Checklist

* [x] ✅ **Source & build instructions** (`README.md`) — end-to-end reproducible
* [x] ✅ **data/** — JSON file(s) containing ≥ 150 validated Q\&A pairs (`cli_qa_dataset.json`)
* [x] ✅ **Training script + LoRA adapter files** (`model.py`, `lora_adapter/` ≤ 500 MB)
* [x] ✅ **agent.py** — Runnable as: `python agent.py "Create a new Git branch and switch to it"`
* [x] ✅ **eval\_static.md** — Base vs. fine-tuned answers + metrics
* [x] ✅ **eval\_dynamic.md** — Agent runs + 0-2 scoring table
* [x] ✅ **report.md** — One-page summary
* [x] ✅ **Demo video** — ≤ 5 min, Loom/MP4 format

---


