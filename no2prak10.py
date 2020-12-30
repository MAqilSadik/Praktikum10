def inputMhs(source,nim,nama,alamat) :
    tambah = open(source,"a")
    tambah.write("{}|{}|{}\n".format(nim,nama,alamat))
    tambah.close()
def viewMhs(source):
    liat = open(source,'r')
    for i in liat :
        print(i)
    liat.close()

source = "dataMhs"
again = "y"
while again == "y":
    nim = input("masukkan NIM  :")
    nama = input("masukkan nama Mhs  :")
    alamat = input("masukkan alamat  :")
    inputMhs(source,nim,nama,alamat)
    again = input("ulangi input lagi(y/n) :")

if again !="y":
    print("data mahasiswa")
    viewMhs(source)
