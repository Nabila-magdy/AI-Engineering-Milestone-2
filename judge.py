import requests
import json

def judge_answer(question, expected, answer):

    prompt = f"""
    You are an AI evaluator.

    Question: {question}

    Expected Answer: {expected}

    Model Answer: {answer}

    Give a score from 1 to 5.

    5 = Completely correct and includes all important information.
    4 = Correct but missing a small detail.
    3 = Partially correct but missing important information.
    2 = Mostly incorrect or contains major mistakes.
    1 = Completely incorrect or unrelated.

    Important rules:
    - Do not give 5 just because the answer is related to the question.
    - Compare the meaning with the expected answer.
    - Missing important information must reduce the score.
    - Do not reward incorrect information.
    - Evaluate the meaning, not exact words.
    - If an answer misses an essential defining property, its score must not exceed 3.
    - If the answer gives a completely false definition, assign score 1.
    - Do not give partial credit to an answer that contradicts the basic meaning of the concept.

    Return JSON with:
    score and reason.
    """

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0
        }
    }

    response = requests.post(url, json=data)

    result = response.json()["response"]

    evaluation = json.loads(result)

    return evaluation


# Test the judge

if __name__ == "__main__":

    question = "What is a Database?"

    expected = "An organized collection of data."

    answer = "A database stores and organizes information for easy access."

    result = judge_answer(question, expected, answer)

    print("Judge Test")
    print("Score:", result["score"])
    print("Reason:", result["reason"])
    print("--------------------")

    # Judge Calibration Test

    question = "What is RAM?"

    expected = "RAM is temporary memory used by the computer."

    answers = [
        "RAM is temporary memory used by the computer.",
        "RAM is a type of computer memory.",
        "RAM is a programming language."
    ]

    for answer in answers:

        result = judge_answer(question, expected, answer)

        print("Answer:", answer)
        print("Score:", result["score"])
        print("Reason:", result["reason"])
        print("--------------------")
