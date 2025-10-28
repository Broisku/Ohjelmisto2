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
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        else:
            print("Hissi on jo alimmassa kerroksessa")
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, haluttu_kerros):
        if haluttu_kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < haluttu_kerros:
                  self.kerros_ylos()

        elif haluttu_kerros < self.nykyinen_kerros:
             while self.nykyinen_kerros > haluttu_kerros:
                   self.kerros_alas()