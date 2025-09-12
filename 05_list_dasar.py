tamu_undangan = ["Khresna","Asa","Natya"]
print("Tamu undangan awal:", tamu_undangan)

# Tamu pertama tidak bisa datang, ganti dengan tamu baru
tamu_undangan[0] = "Rizky"
print("Tamu undangan setelah diganti :", tamu_undangan)

# Menambahkan tamu baru di akhir list
tamu_undangan.append("Nino")
print("Tamu undangan setelah ditambah :", tamu_undangan)

for tamu in tamu_undangan:
    print("Selamat datang di pesta,", tamu, "!")
