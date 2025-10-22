from classes.car import Auto
import random
from prettytable import PrettyTable
table = PrettyTable()

autot = []

for i in range(10):
    huippunopeus = random.randint(100,200)
    autot.append(Auto("ABC-" + str(i+1), huippunopeus))

while max(auto.matka for auto in autot) < 10_000:
    for auto in autot:
        auto.kulje(1)
        auto.kiihdyta(random.randint(-10, 15))
    kokonaismatka = sum(auto.matka for auto in autot)

table.field_names = ["rekisteritunnus", "huippunopeus", "nopeus", "matka"]
for auto in autot:
    table.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka])

print(table)