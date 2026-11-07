import subprocess
import sys

print("Starting Automated Evaluation...")

result = subprocess.run(
    [sys.executable, "evaluate.py"]
)

if result.returncode == 0:
    print("Evaluation completed successfully!")
else:
    print("Evaluation failed!")
    sys.exit(1)