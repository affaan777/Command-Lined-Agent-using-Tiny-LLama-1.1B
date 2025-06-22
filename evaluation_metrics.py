# eval_metrics.py — Compute ROUGE-L scores for each prompt
from rouge_score import rouge_scorer

# List of (base_output, fine_tuned_output) pairs
pairs = [
    ("git branch new-branch-name && git checkout new-branch-name",
     "git checkout -b new-branch-name"),

    ("tar -zcvf reports.tar.gz reports",
     "tar cf - {} reports.tar.gz"),

    ("Uses os.walk in a Python script to list files",
     "find . -type f -name '*.py'"),

    ("python3 -m venv venv && source venv/bin/activate && pip install requests",
     "python -m venv myenv && source myenv/bin/activate && pip install requests"),

    ("sed + find to get output.log lines",
     "tail -n 10 output.log"),

    ("tar -xzvf file.tar.gz",
     "tar xzf {path/to/file.tar.gz}"),

    ("Full bash script with metadata",
     "ls -lh /path/to/dir")
]

scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

print("\n📊 ROUGE-L Scores (F1):\n")
for i, (base, tuned) in enumerate(pairs, 1):
    score = scorer.score(base, tuned)
    print(f"Prompt {i}: {score['rougeL'].fmeasure:.4f}")

# Optionally: compute average ROUGE-L
avg = sum(scorer.score(b, t)['rougeL'].fmeasure for b, t in pairs) / len(pairs)
print(f"\n📈 Average ROUGE-L: {avg:.4f}")
