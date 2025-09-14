# Ini adalah variabel global
nama_global = "Budi"

def sapa_teman():
    # Ini adalah variabel lokal
    nama_lokal = "Ani"
    print(f"Di dalam fungsi, menyapa {nama_lokal}")
    print(f"Di dalam fungsi, bisa mengakses nama global: {nama_global}")

# Memanggil fungsi
sapa_teman()

print(f"\nDi luar fungsi, bisa mengakses nama global: {nama_global}")
# print(f"Di luar fungsi, mencoba mengakses nama lokal: {nama_lokal}") # BARIS INI AKAN ERROR!
