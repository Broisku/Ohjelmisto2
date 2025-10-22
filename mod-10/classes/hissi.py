class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        else:
            print("Hissi on jo ylimmässä kerroksessa")
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > alin_kerros:
            self.nykyinen_kerros -= 1
        else:
            print("Hissi on jo alimmassa kerroksessa")
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, haluttu_kerros):
        nykyinen_kerros = self.nykyinen_kerros
        if haluttu_kerros > nykyinen_kerros:
            while nykyinen_kerros < haluttu_kerros:
                  Hissi.kerros_ylos(self)

        elif haluttu_kerros < nykyinen_kerros:
             while nykyinen_kerros > haluttu_kerros:
                   Hissi.kerros_alas(self)