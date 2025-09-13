class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
        print(f"Sebuah kucing bernama {nama} baru saja dibuat!")
      
    def info_kucing(self):
        print(f"Kucing ini bernama {self.nama}, berwarna {self.warna}, dan berumur {self.umur} tahun.")
      
# Membuat objek pertama dari class Kucing
kucing1 = Kucing("Oren,", "Oranye", 2)
kucing2 = Kucing("Kitty", "Putih", 1)

print("\n--- Info Kucing ---")
print("Kucing 1 adalah", kucing1.nama, "berwarna", kucing1.warna, "dan berumur", kucing1.umur, "tahun")
print("Kucing 2 adalah", kucing2.nama, "berwarna", kucing2.warna, "dan berumur", kucing2.umur, "tahun")

kucing1.info_kucing()

