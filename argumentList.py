# Belajar Argument List

def operasiMatematika(operasi="", *listAngka):
    xhasil = 0
    yhasil = 1
    for angka in listAngka:
        if operasi=="tambah" :
            xhasil = xhasil + angka
        elif operasi=="perkalian" :
            yhasil = yhasil * angka
    print(f"Hasil {operasi} adalah {xhasil} atau {yhasil}")

operasiMatematika("perkalian", 5,3,8,4)
