from classes.car import Auto

auto = Auto("123-ABC", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"""
rekisteritunnus: {auto.rekisteritunnus}
huippunopeus: {auto.huipppunopeus}
nopeus: {auto.nopeus}
matka: {auto.matka}""")

auto.kiihdytä(-200)

print(f"nopeus: {auto.nopeus}")