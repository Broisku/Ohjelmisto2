class Auto:
    def __init__(self, new_rekisteritunnus, new_huippunopeus):
        self.rekisteritunnus = new_rekisteritunnus
        self.huippunopeus = new_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka = self.matka + self.nopeus * aika