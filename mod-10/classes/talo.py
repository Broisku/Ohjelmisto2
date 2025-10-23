from classes.hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissit_lkm):
        self.haluttu_kerros = None
        self.hissin_numero = None
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit_lkm = hissit_lkm
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissit_lkm)]

    def aja_hissia(self, hissin_numero, haluttu_kerros):
        self.hissin_numero = hissin_numero
        self.haluttu_kerros = haluttu_kerros
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(haluttu_kerros)