from classes.julkaisu import Lehti, Kirja

p1 = "Aku Ankka"
p2 = "Aki Hyyppä"

lehti = Lehti(p1, p2)

p3 = "Hytti n:o 6"
p4 = "Rosa Liksom"
p5 = 200

kirja = Kirja(p3, p4, p5)

lehti.tulosta_tiedot()
print("")
kirja.tulosta_tiedot()