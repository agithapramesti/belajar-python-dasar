# Belajar Set -> nyimpan data lebih dari 1

# list : []
# tuple : ()
# set : {}

nama = {"Gege", "Rani", "Megan"}
print(nama)

# apa bedanya dgn tuple dan list ?
# kalo di set, data harus UNIK, gabisa sama

nama = {"Gege", "Rani", "Rani","Gege", "Andi"}
print(nama)

# dalam set, kita gabisa akses data pake index. karna posisinya bisa berubah
# mengubah data pake index juga gabisa, yg bisa cuma menambah data dan hapus

nama.add("MomoGi")
for i in nama:
    print(i)

print("-- remove --")

nama.remove("MomoGi")
for i in nama:
    print(i)
