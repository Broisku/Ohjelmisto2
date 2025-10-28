from classes.car import Auto
import random
from prettytable import PrettyTable

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kulje(1)
            auto.kiihdyta(random.randint(-10, 15))

    def tulosta_tilanne(self):
        table = PrettyTable()
        table.field_names = ["rekisteritunnus", "huippunopeus", "nopeus", "matka"]
        for auto in self.autot:
            table.add_row([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka])
        print(table)

    def kilpailu_ohi(self):
        if max(auto.matka for auto in self.autot) >= self.pituus:
            print("kilpailu päättyi: lopputulokset:")
            return True
        else:
            return False