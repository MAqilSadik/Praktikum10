def toCaesar(source,key):
    hasil = ''
    file = open(source,'r')
    for i in file.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) + key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) + key - 65) % 26 + 65)
    file.close()
    fileEnc = open(source+'.encrypt','w')
    fileEnc.write(hasil)
    fileEnc.close()
    print('File enkripsi : {}.encrypt'.format(source))

source = input('Nama file yang ingin di enkripsi : ')
key = int(input('Input Key : '))
toCaesar(source,key)
