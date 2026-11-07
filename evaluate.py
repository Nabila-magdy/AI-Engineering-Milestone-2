import requests
import sys
from test_cases import test_cases
from judge import judge_answer

url = "http://localhost:11434/api/generate"

passed = 0
failed = 0

final_passed = 0
final_failed = 0

total_score = 0
total = len(test_cases)

for test in test_cases:

    data = {
        "model": "qwen2.5:1.5b",
        "prompt": test["question"],
        "stream": False
    }

    response = requests.post(url, json=data)
    answer = response.json()["response"]

    expected = test["expected"]

    # Programmatic Validation
    if expected.lower() in answer.lower():
        print("Programmatic Result: PASS")
        passed += 1
    else:
        print("Programmatic Result: FAIL")
        failed += 1

    # LLM Judge
    evaluation = judge_answer(
        test["question"],
        expected,
        answer
    )

    score = int(evaluation["score"])
    if score < 1 or score > 5:
        raise ValueError("Judge score must be between 1 and 5")
    total_score += score

    if score >= 4:
        print("Final Result: PASS")
        final_passed += 1
    else:
        print("Final Result: FAIL")
        final_failed += 1

    print("Judge Score:", score, "/ 5")
    print("Judge Reason:", evaluation["reason"])

    print("--------------------")

# Final Report
pass_rate = (final_passed / total) * 100
average_score = total_score / total

print("Total Tests:", total)
print("Programmatic Passed:", passed)
print("Programmatic Failed:", failed)
print("Final Passed:", final_passed)
print("Final Failed:", final_failed)
print("Final Pass Rate:", pass_rate, "%")
print("Average Judge Score:", average_score, "/ 5")

# CI/CD Result
if final_failed > 0:
    sys.exit(1)
else:
    print("All tests passed successfully!")