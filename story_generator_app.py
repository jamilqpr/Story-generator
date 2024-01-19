import requests
import json

api_key = 'AIzaSyBPmwo4aIXtvz2nfPVzF_ucRKAuUCvvTEk'
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + api_key

headers = {'Content-Type': 'application/json'}

data = {
    "contents": [
        {
            "parts": [
                {"text": "Write a story about a magic backpack"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

# Save the response to a text file
with open('generated_story.txt', 'w', encoding='utf-8') as file:
    file.write(result['candidates'][0]['content']['parts'][0]['text'])

print("Generated story saved to 'generated_story'")
