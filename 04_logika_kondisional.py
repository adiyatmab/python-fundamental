# Latihan 4.1: Pengecekan Kategori Umur
umur = 19
if umur >= 18:
    print("Anda termasuk kategori Dewasa.")
elif umur >= 13:
    print("Anda termasuk kategori Remaja.")
else:
    print("Anda termasuk kategori Anak-anak.")

print("\n" + "="*20 + "\n") # Ini hanya baris pemisah agar output rapi

# Latihan 4.2: Pengecekan Syarat Rekrutmen
memiliki_ijazah_s1 = True
pengalaman_kerja_tahun = 1

if (memiliki_ijazah_s1 and pengalaman_kerja_tahun >= 1) or pengalaman_kerja_tahun >=3:
    print("Kandidat memenuhi syarat untuk wawancara.")
else:
    print("Maaf, kandidat belum memenuhi syarat.")
