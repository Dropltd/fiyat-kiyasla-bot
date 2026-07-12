import json
import requests


URL = "https://bim.veesk.net/service/v1.0/home/aktuel"

HEADERS = {
    "Content-Type": "application/json",
    "X-App-version": "20241101"
}


def run():
    response = requests.post(
        URL,
        headers=HEADERS,
        json={"token": ""},
        timeout=30,
    )

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        return

    data = response.json()

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("output.json oluşturuldu.")
