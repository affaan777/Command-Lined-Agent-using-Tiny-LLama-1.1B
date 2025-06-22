📊 eval_static.md – Base vs. Fine-Tuned Output Comparison

This file documents the evaluation of the fine-tuned TinyLlama model against its base model using 7 standard prompts. Plan scores (0–2) reflect the clarity, correctness, and executability of answers.

Create a new Git branch and switch to it.

Base:

git branch new-branch-name
git checkout new-branch-name ```

Fine-Tuned:

git branch my-new-branch
git checkout my-new-branch

Plan Score: Base = 2, Fine-Tuned = 2

2. Compress the folder reports into reports.tar.gz.

Base:

tar -zcvf reports.tar.gz reports

Fine-Tuned:

tar cf - {} reports.tar.gz

Plan Score: Base = 2, Fine-Tuned = 1 (find-based version is overcomplicated)

3. List all Python files in the current directory recursively.\*\*

Base: Uses Python script with os.walk
Fine-Tuned:

find . -type f -name '\*.py'

Plan Score: Base = 1 (too verbose), Fine-Tuned = 2

---

4. Set up a virtual environment and install requests.

Base:
python3 -m venv venv
source venv/bin/activate
pip install requests

Fine-Tuned:
python -m venv myenv && source myenv/bin/activate && pip install requests

Plan Score: Base = 2, Fine-Tuned = 2

5. Fetch only the first ten lines of a file named output.log.

Base: ❌ Incorrect (uses sed and find for a simple task)
Fine-Tuned:
tail -n 10 output.log

Plan Score: Base = 0, Fine-Tuned = 2

6. Edge Case: How to unzip a .tar.gz file?

Base: tar -xzvf file.tar.gz
Fine-Tuned:
tar xzf {path/to/file.tar.gz}
Plan Score: Base = 2, Fine-Tuned = 2

7.Edge Case: How to list files in a directory using Bash?

Base: Full Bash script (verbose)
Fine-Tuned:
ls -lh /path/to/dir
Plan Score: Base = 1, Fine-Tuned = 2

✅ The fine-tuned model consistently produces cleaner, more focused CLI answers.

📊 ROUGE-L Scores (F1):

Prompt 1: 0.6250
Prompt 2: 0.7273
Prompt 3: 0.0000
Prompt 4: 0.7273
Prompt 5: 0.3333
Prompt 6: 0.6667
Prompt 7: 0.0000

📈 Average ROUGE-L: 0.4399

| Prompt | ROUGE-L | Base Score | Fine-Tuned Score |
| ------ | ------- | ---------- | ---------------- |
| 1      | 0.6250  | 2          | 2                |
| 2      | 0.7273  | 2          | 1                |
| 3      | 0.0000  | 1          | 2                |
| 4      | 0.7273  | 2          | 2                |
| 5      | 0.3333  | 0          | 2                |
| 6      | 0.6667  | 2          | 2                |
| 7      | 0.0000  | 1          | 2                |

Average ROUGE-L: 0.4399  
Average Base Score: 1.43  
Average Fine-Tuned Score: 1.86
