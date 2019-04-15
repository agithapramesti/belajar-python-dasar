# Membuat program sederhana dengan for loop, list, dan range

banyak = int(input("masukkan banyak data>> "))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i+1}")
    nama.append(input("Masukkan Nama: "))
    umur.append(int(input("Masukkan Umur: ")))

print("-- Hasil --")

for i in range(0, len(nama)):
    print(f"{nama[i]} berusia {umur[i]} tahun")
