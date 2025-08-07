import requests

url = "http://localhost:8000/hackrx/run"
headers = {
    "Authorization": "Bearer 5567e44f0baf1876abcb15031a2c1f25dcf5268280928d3c94cc955c52b8f99c",
    "Content-Type": "application/json"
}

data = {
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": [
        "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
        "Does this policy cover maternity expenses, and what are the conditions?"
    ]
}

response = requests.post(url, headers=headers, json=data)

print("Raw Gemini Response:", response.text)
response.raise_for_status()
data = response.json()
