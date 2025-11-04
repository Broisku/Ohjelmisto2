import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

try:
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["value"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")