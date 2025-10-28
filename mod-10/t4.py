from classes.kilpailu import Kilpailu
from classes.car import Auto
import random

autot = []

for i in range(10):
    huippunopeus = random.randint(100,200)
    autot.append(Auto("ABC-" + str(i+1), huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

count = 0

while True:
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi():
        autot.sort(key=lambda car: car.matka, reverse=True)
        kilpailu.tulosta_tilanne()
        break
    if count % 10 == 0:
        autot.sort(key=lambda car: car.matka, reverse=True)
        kilpailu.tulosta_tilanne()
        print("")
    count += 1