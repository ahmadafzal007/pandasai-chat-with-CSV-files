import requests

data = {
    "prompt": "Hello"
}

response = requests.post("http://localhost:11434/api/generate", json=data)
print(response.text)
