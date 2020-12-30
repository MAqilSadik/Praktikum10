cariNIMMhs = input('Masukkan NIM yang dicari :')
file = open('dataMhs', 'r')
a = file.readlines()

for i in range(len(a)) :
    if(cariNIMMhs in a[i]) :
        keterangan = 'y'
        break
    else :
        keterangan = 'n'
        continue
if(keterangan == 'y') :
        n = a[i].split('|')
        print('\nData Mahasiswa')
        print('NIM    :', n[0])
        print('Nama   :', n[1])
        print('Alamat :', n[2])
else :
    print('Data mahasiswa tidak ditemukan')
