# Belajar return value

def operasiMatematika(operasi="", *listAngka):
    xHasil = 0
    yHasil = 1
    for angka in listAngka :
        if operasi == "tambah" :
            xHasil = xHasil + angka
        elif operasi == "kurang" :
            xHasil = angka - xHasil
        elif operasi == "kali" :
            yHasil = yHasil * angka
        else:
            yHasil = angka/yHasil
    if xHasil != 0 :
        return (listAngka, xHasil)
    else:
        return (listAngka, yHasil)

listAngka, hasil = operasiMatematika("kali", 9,5,2,1)

print(f"Hasil {listAngka} adalah {hasil}") #pengimplementasian tuple
    