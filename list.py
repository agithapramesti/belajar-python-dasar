# Belajar List

# Menambah Data dalam List
nama = []
nama.append("Gege")
nama.append("Megan")
nama.append("Shirley")
nama.append("Stella")

nama2 = ["Grelly", 'Rani']
nama2.append("Fara")
nama2.append("Dea")

# Mengakses Data pada index ke-
print(nama)
print(nama[1])
print(nama2)
print(nama2[2])

# length dalam list = len
print("Jumlah List Nama: ")
print(len(nama))

# Hapus data dalam list
nama.remove("Megan")
print(nama)

# Ubah Data
nama[0] = "Kimmy"
print(nama)