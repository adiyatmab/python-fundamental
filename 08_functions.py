def hitung_luas_persegi(panjang, lebar):
  """Fungsi ini menghitung luas persegi."""
  luas = panjang * lebar
  print("Luas persegi dengan panjang adalah", luas)

hitung_luas_persegi(5, 10)
hitung_luas_persegi(7, 3)

def hitung_harga_setelah_diskon(harga_awal, persen_diskon):
    """Fungsi ini menghitung harga setelah diskon dan MENGEMBALIKAN nilainya."""
    potongan = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - potongan
    return harga_akhir

harga_dibayar = hitung_harga_setelah_diskon(500000,15)
print("Harga yang harus dibayar setelah diskon adalah: Rp", harga_dibayar)
