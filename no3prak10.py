def mhs(dataMhs):
    data = open("dataMhs",'r')
    mhs = data.read().splitlines()
    dataMhs = {}
    hitungan = 1
    for i in mhs:
        x = i.split('|')
        dataMhs[hitungan] = {'nim': x[0], 'nama': x[1], 'alamat': x[2]}
        hitungan +=1
    print(dataMhs)
    return dataMhs

source = "dataMhs"
mhs(source)
