def decCaesar(source,key):
    hasil = ''
    file = open(source,'r')
    for i in file.read():
        if i == ' ':
            hasil += i
        elif i.islower():
            hasil += chr((ord(i) - key - 97) % 26 + 97)
        else:
            hasil += chr((ord(i) - key - 65) % 26 + 65)
    file.close()
    fileDnc = open(source+'.decrypt','w')
    fileDnc.write(hasil)
    fileDnc.close()
    print('File dekripsi : {}.decrypt'.format(source))

source = input('Nama file yang ingin di dekripsi : ')
key = int(input('Input Key : '))
decCaesar(source,key)
