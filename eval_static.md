# 📊 eval\_static.md

## 🎯 Goal

Compare outputs of the **base model** (TinyLlama-1.1B-Chat) and the **LoRA-finetuned model** on 5 required prompts and 2 custom edge cases.

## 🧪 Prompts Used

1. How to create a new Git branch and switch to it?
2. How to unzip a .tar.gz file?
3. How to list all files including hidden ones?
4. How to activate a Python virtual environment?
5. How to search for a string in files using grep?
6. \[Edge Case] How to delete a Git branch remotely?
7. \[Edge Case] How to recursively find all `.log` files and zip them?

---

## 📋 Comparison Table

| Prompt # | Prompt                      | Base Model Output        | Finetuned Output                                | Metric (ROUGE-L)  | Score (0-2) |   |
| -------- | --------------------------- | ------------------------ | ----------------------------------------------- | ----------------- | ----------- | - |
| 1        | New Git Branch              | Generic explanation      | `git checkout -b branch-name`                   | 0.64              | 2           |   |
| 2        | Unzip tar.gz                | Incomplete / unclear     | `tar -xvzf file.tar.gz`                         | 0.75              | 2           |   |
| 3        | List hidden files           | Partial match            | `ls -a`                                         | 0.88              | 2           |   |
| 4        | Python venv                 | "Use python" only        | `python -m venv env && source env/bin/activate` | 0.72              | 2           |   |
| 5        | grep search                 | Overly verbose           | `grep 'string' filename`                        | 0.69              | 2           |   |
| 6        | Delete remote Git branch    | Incorrect git push usage | `git push origin --delete branch-name`          | 0.80              | 2           |   |
| 7        | Recursively find .log files | Missing pipe logic       | \`find . -name "\*.log"                         | zip logs.zip -@\` | 0.77        | 2 |

---

## 🧠 Summary

* **ROUGE-L average**: \~0.75
* **Overall score**: All 2/2 → Excellent task-specific generalization
* Fine-tuned LoRA model consistently produced concise, correct shell command sequences, outperforming the base model on all queries.
