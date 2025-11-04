import requests
import json

paikkakunta = input("Syötä paikkakunta: ")
print("")


response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=beeeb47fee41a64ae7011f133b74fd18&units=metric&lang=fi")

try:
    if response.status_code == 200:

        json_response = response.json()

        print("Olosuhteet:")
        for i in json_response["weather"]:
            print(i["description"])

        print("")

        print("Lämpötila (celsius):")
        print(json_response["main"]["temp"])


except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")