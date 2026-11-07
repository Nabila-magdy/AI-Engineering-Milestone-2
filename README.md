# AI Engineering – Milestone 2
## Automated Regression Evaluation Suite

### 1. Project Overview
This project implements an automated evaluation pipeline to test the performance and correctness of a locally running Large Language Model (LLM).

The system evaluates model answers using two methods:
- Programmatic Validation.
- LLM-as-a-Judge.

### 2. Project Objectives
- Create 30 golden test cases.
- Automatically test the model's answers.
- Validate answers using programmatic assertions.
- Evaluate answer quality using an LLM judge.
- Calculate pass/fail rates and average evaluation scores.
- Run the evaluation through a Python test runner.

### 3. Tools and Technologies
- Python 3.11
- Ollama
- Qwen 2.5 – 1.5B
- Requests Library
- JSON

### 4. Evaluation Methodology

**A. Programmatic Validation**

The system compares the model's answer with the expected keyword using Python string matching.

**B. LLM-as-a-Judge**

A second evaluation step uses the Qwen model to score each answer from 1 to 5 based on correctness and completeness.

- Score 5: Completely correct.
- Score 4: Correct with a minor missing detail.
- Score 3: Partially correct.
- Score 2: Mostly incorrect.
- Score 1: Completely incorrect.

A score of 4 or higher is considered a PASS.

### 5. Project Structure

| File | Description |
|---|---|
| `test_model.py` | Tests the local model connection. |
| `test_cases.py` | Contains 30 golden test cases. |
| `judge.py` | Implements the LLM-as-a-Judge evaluator. |
| `evaluate.py` | Runs the evaluation pipeline and calculates results. |
| `run_tests.py` | Runs the evaluation and checks its exit status. |
| `results.txt` | Contains the detailed evaluation results. |

### 6. How to Run the Project

**Requirements:**
- Python 3.11
- Ollama installed and running.
- Qwen 2.5 – 1.5B model downloaded.
- Requests library installed.

Install the required library:

```bash
py -3.11 -m pip install requests
```

Run the automated evaluation:

```bash
py -3.11 run_tests.py
```

### 7. Evaluation Results

The project was evaluated using 30 test cases.

| Metric | Result |
|---|---:|
| Total Test Cases | 30 |
| Programmatic Passed | 22 |
| Programmatic Failed | 8 |
| Final Passed | 25 |
| Final Failed | 5 |
| Final Pass Rate | 83.33% |
| Average Judge Score | 4.33 / 5 |

### 8. Conclusion

The project successfully demonstrates an automated regression evaluation pipeline for a locally running language model.

It combines programmatic validation with LLM-based judging to assess answer correctness and quality.

The evaluation achieved an 83.33% final pass rate, identifying areas where the model's answers need improvement.# AI-Engineering-Milestone-2
