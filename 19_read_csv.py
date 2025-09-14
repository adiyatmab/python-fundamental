import csv

with open('data_mahasiswa.csv', mode='r') as file:
    # Create a csv reader object
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)
    print(f"Header: {header}")
    
    # Loop through the remaining rows
    print("\nData Mahasiswa:")
    for row in csv_reader:
        print(f"NIM: {row[0]}, Nama: {row[1]}, Jurusan: {row[2]}")

   for row in csv_reader:
        if row[2] == 'Informatika':
            print(f"NIM: {row[0]}, Nama: {row[1]}, Jurusan: {row[2]}")
