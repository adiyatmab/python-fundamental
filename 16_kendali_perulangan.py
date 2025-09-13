daftar_nilai = [85, 92, -5, 78, 999, 100, 45]
for nilai in daftar_nilai:
    if nilai == 999:
        print("Nilai 999 ditemukan! Menghentikan proses.")
        break
    elif nilai < 0:
        print("Nilai tidak valid:", nilai)
        continue
    else:
        print("Memproses nilai:", nilai)
