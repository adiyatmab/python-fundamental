# 'r' berarti mode 'read' (baca)
with open("biodata.txt","r") as file:
    # .read() akan membaca seluruh isi file sebagai satu string
    isi_biodata = file.read()

print("--- Isi dari biodata.txt ---")
print(isi_biodata)
print("--- Selesai membaca ---")

# Blok pertama: Menulis dan menimpa file
with open("laporan.txt", "w") as file:
    # Pastikan baris ini menjorok ke dalam persis seperti ini
    file.write("Laporan Harian\n")
    file.write("Status: Semua sistem berjalan normal.\n")

# Blok kedua: Menambahkan ke file yang ada
with open("laporan.txt", "a") as file:
    # Pastikan baris ini juga menjorok ke dalam
    file.write("Tindakan selanjutnya: Tidak ada")

# Blok ketiga: Membaca dan menampilkan hasil akhir
with open("laporan.txt", "r") as file:
    # Pastikan baris ini juga menjorok ke dalam
    print(file.read())
