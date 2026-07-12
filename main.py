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

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON kaydedildi.")
