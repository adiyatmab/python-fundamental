# Class Induk (Parent Class)
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan ini mengeluarkan suara...")

# Class Anak (Child Class) yang MEWARISI dari Hewan
class Anjing(Hewan):
    def bersuara(self): # Method ini menimpa (override) method induk
        print(f"{self.nama} bilang: Guk Guk!")

# Class Anak lainnya
class Kucing(Hewan):
    def bersuaras(self): # Method ini tidak menimpa method induk
        print(f"{self.nama} bilang: Meow!")

hewan_umum = Hewan("Misterius")
anjing_peliharaan = Anjing("Doggo")
kucing_peliharaan = Kucing("Kitty") # Akan mengambil dari class induk

hewan_umum.bersuara()
anjing_peliharaan.bersuara()
kucing_peliharaan.bersuara()
