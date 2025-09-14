# Membuat set dari sebuah list yang memiliki data duplikat
daftar_angka = [1, 2, 2, 3, 4, 4, 4, 5]
set_unik = set(daftar_angka)

print("List awal:", daftar_angka)
print("Set yang dihasilkan:", set_unik) # Perhatikan, semua duplikat hilang

# Menambah elemen ke set
set_unik.add(6)
print("Setelah ditambah 6:", set_unik)

# Mencoba menambah elemen yang sudah ada
set_unik.add(1)
print("Setelah mencoba menambah 1 lagi:", set_unik) # Tidak ada yang berubah
