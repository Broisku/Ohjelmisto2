from classes.car import Auto

auto = Auto("123-ABC", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"""
rekisteritunnus: {auto.rekisteritunnus}
huippunopeus: {auto.huippunopeus}
nopeus: {auto.nopeus}
matka: {auto.matka}""")

auto.kiihdyta(-200)

print(f"nopeus: {auto.nopeus}")