import requests

url = "https://78c43c988331.ngrok-free.app/hackrx/run"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 5567e44f0baf1876abcb15031a2c1f25dcf5268280928d3c94cc955c52b8f99c"
}
payload = {
    "documents": "https://example.com/sample.pdf",
    "questions": ["What is covered in the maternity policy?"]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.json())
