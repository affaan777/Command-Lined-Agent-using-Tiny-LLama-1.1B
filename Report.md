# 📄 Report – AI/ML Internship Technical Task

**Candidate:** Mohammed Affaan Shaikh
**Task:** TinyLlama LoRA Fine-Tuning + CLI Agent

---

## 🎯 Objective

To build an intelligent command-line assistant by:

* Curating 150+ real-world Q\&A pairs on Git, Bash, tar/gzip, grep, venv, etc.
* Fine-tuning a lightweight LLM (`TinyLlama/TinyLlama-1.1B-Chat-v1.0`) using LoRA
* Wrapping the model into a usable `agent.py` CLI interface
* Evaluating model improvements through metrics and user testing

---

## 📚 Data Collection

**Sources Used:**

* Stack Overflow, TLDR.sh, explainshell.com, GitHub Issues, Ubuntu Forums
* Manually curated and verified

**Size:** 150 validated Q\&A pairs
**Format:** JSON — `{ "question": "...", "answer": "..." }`

---

## 🔧 Model & Training Details

**Model:** TinyLlama-1.1B-Chat-v1.0
**Technique:** LoRA Fine-Tuning (Low-Rank Adaptation)
**Library Stack:** `transformers`, `peft`, `datasets`, `torch`, `Trainer`

**Hyperparameters:**

* Epochs: 1
* Batch Size: 2 (CPU training)
* Learning Rate: 2e-4
* Max Length: 256 tokens

**Training Time:** \~30 minutes (Intel CPU, local machine)

**Output:** `lora_adapter/` (LoRA weights only, ≤ 500MB)

---

## 🤖 CLI Agent Wrapper

* Input: Natural language instruction from user
* Output: Step-by-step shell plan
* Command Detection: Executes `echo <cmd>` if command is first line
* Logs saved to `logs/trace.jsonl`
* Supports batch queries and interactive mode

---

## 📈 Evaluation Summary

### Static Evaluation (ROUGE-L F1)

| Prompt                      | ROUGE-L |
| --------------------------- | ------- |
| Create Git branch           | 0.6250  |
| Compress folder             | 0.7273  |
| List Python files           | 0.0000  |
| Set up venv + requests      | 0.7273  |
| Show first 10 lines         | 0.3333  |
| Unzip .tar.gz file          | 0.6667  |
| List files in directory     | 0.0000  |
| **Average ROUGE-L:** 0.4399 |         |

### Dynamic Evaluation (Plan Quality)

| Prompt                                   | Score (0–2) |
| ---------------------------------------- | ----------- |
| Git branch + switch                      | 2           |
| Compress folder                          | 1           |
| List Python files                        | 2           |
| venv + requests                          | 2           |
| Read first 10 lines                      | 2           |
| Unzip .tar.gz                            | 2           |
| List files                               | 2           |
| **Total Score:** 13/14 → **Avg: 1.86** ✅ |             |

---

## 💡 Future Improvements

1. **Multi-Turn Dialogue Support:** Enable the agent to handle context retention and chained commands.
2. **Real Execution Sandbox:** Dry-run with actual subprocess integration for execution & validation.

---

## ✅ Final Deliverables

* `cli_qa_dataset.json` – 150+ CLI Q\&A
* `agent.py` – CLI model agent
* `lora_adapter/` – Fine-tuned adapter weights
* `eval_static.md` / `eval_dynamic.md` – Evaluation
* `eval_metrics.py` – ROUGE score calculator
* `report.md` – This summary
* `demo.mp4` – Live walkthrough

---
