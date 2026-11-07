import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5:1.5b",
    "prompt": "What is Python?",
    "stream": False
}

response = requests.post(url, json=data)

answer = response.json()["response"]

print(answer)