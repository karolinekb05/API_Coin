import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.coinbase.com/v2/prices/spot"
# Informa o header da requisição
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
}
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
}
# Faz a requisição
response = requests.post(url, headers=headers, data=json.dumps(data))
# Converte a resposta para json
print(response.json())