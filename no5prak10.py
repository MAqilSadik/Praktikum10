def penjumlahan(sumber):
    data = open(sumber,"r")
    for i in data:
        pecah = i.split('|')
        result = int(pecah[0])+int(pecah[1])
        print(result)
    data.close()

sumber = "bilangan.txt"
penjumlahan(sumber)
