def tambahMundur(x,y):
    if x.isnumeric() or x.isnumeric() and int(x) <=359999:
        b = x[::-1].split() #balikkan input x
        b.reverse()
        b = ''.join(b)
        
        c = y[::-1].split() #membalikkan input y
        c.reverse()
        c = ''.join(c)
        d = int(b)+int(c)

        e = list(str((d))) #membalikkan hasil penjumlahan
        e.reverse()
        e = ''.join(e)
        print('Hasil Tambah Mundurnya :',(e))
    else:
        print('Invalid Input')
    
    return e

x = input('Masukkan Angka 1 : ')
y = input('Masukkan Angka 2 : ')
#angka2 = int(input('Masukkan Angka 2 : '))

tambahMundur(x,y)

'''Masukkan angka 1 : 24
Masukkan angka 2 : 1
Hasil tambah mundurnya : 34
Masukkan angka 1 : 4358
Masukkan angka 2 : 754
Hasil tambah mundurnya : 1998
Masukkan angka 1 : 1234
Masukkan angka 2 : 5678
Hasil tambah mundurnya : 68031'''
