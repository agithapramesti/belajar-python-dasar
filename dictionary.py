# Belajar Dictionary -> Menyimpan lebih dari 1 data

# perbedaan dari list, tuple, dan set:

customer = {"Nama": "Agitha Pramesti", "Usia": "22 Tahun", "Alamat": "Yogyakarta"}

print(customer)
print("-------")

for data in customer:
    print(data) # ini baru key nya aja blm value nya
print("-------")

for data in customer:
    value = customer[data]
    print(f"{data} = {value}")
print("-------")

# di dictionary ada method namanya items
print(customer.items()) #ini tu tuple-nya
print("--------")

for data in customer.items() :
    print(f"{data[0]} = {data[1]}")
print("-------")

for data, value in customer.items():
    print(f"{data} = {value}")
print("-------")

# kita bisa tambah data di dictionary
customer["Gender"] = "Perempuan"
for data, value in customer.items():
    print(f"{data} = {value}")
print("-------")

# kita bisa hapus data di dictionary
del customer["Gender"]

for data, value in customer.items():
    print(f"{data} = {value}")
print("-------")