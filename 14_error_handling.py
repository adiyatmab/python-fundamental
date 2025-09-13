try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")
except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka.")
