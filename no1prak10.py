def membaca(sumber):
    file = open(sumber, 'r')
    ganjil = 0
    genap = 0
    for i in file:
        if int(i) % 2 == 0:
            genap += 1
        else:
            ganjil += 1
    file.close()
    hasil = {"genap" : genap, "ganjil" :ganjil}
    return hasil
sumber =("datano1.txt")
print("Banyaknya bilangan genap :", membaca(sumber).get('genap'))
print("Banyaknya bilangan ganjil :", membaca(sumber).get('ganjil'))

