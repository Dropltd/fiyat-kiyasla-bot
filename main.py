import requests

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

print(response.status_code)
print(response.text[:3000])
