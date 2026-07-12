import requests
import json

url = "https://bim.veesk.net/service/v1.0/home/aktuel"

headers = {
    "Content-Type": "application/json",
    "X-App-version": "20241101"
}

response = requests.post(
    url,
    headers=headers,
    json={"token": ""}
)

data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))
