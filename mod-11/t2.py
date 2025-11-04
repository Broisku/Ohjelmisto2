from classes.auto import Sahkoauto, Polttomoottoriauto

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kulje(130, 3)
polttomoottoriauto.kulje(140, 3)

print("Matkamittarilukemat:")
print(f"Sähköauto: {sahkoauto.matka}")
print(f"Polttomoottoriauto: {polttomoottoriauto.matka}")