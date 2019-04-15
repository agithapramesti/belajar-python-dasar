# Belajar Break -> ngestop perulangan

for i in range(1,100):
    if( i%2 == 0):
        break
    print(i)

while True:
    data = input("Masukkan Data: ")
    if( data == "x"):
        break
    print("Bukan 'x' !")