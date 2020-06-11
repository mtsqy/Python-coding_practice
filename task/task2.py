# example
HargaBarang = {
    'pulpen': 3000,
    'buku': 3500,
    'kertas_HVS': 40000,
    'map': 5000,
    'spidol': 9500
    }
while True:
    print('masukan nama barang: ', end='')
    nama = input()
    if nama == '':
        break
    if nama in HargaBarang:
        print('Harganya adalah: Rp ', HargaBarang[nama])
    else:
        print('Nama barang' +nama+ 'belum ada di daftar harga')
        harga = int(input('harga barang: Rp '))
        HargaBarang[nama] = harga
        print('Database harga barang telah diupdate')

# task 1
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(10, 40) if x not in noprimes]
A = set(primes)
B = {1,3,4,9,16,25,36,49,64}
intersec = B.intersection(A)
u = A.union(B)
lenofA = len(A)
sums = (sum(A)+sum(B))
difofAandB = A.difference(B)
print(lenofA)
print(intersec)
print(sums)
print(difofAandB)

# task 2
import random
siswa = {'John','Bob','Foo','Bar','James','Rica','Doe','Coady','Alexander','Tim'}
tinggiSiswa = {k: random.randint(155,185) for k in siswa}
while True:
    print('masukan nama siswa: ', end='')
    nama = input()
    if nama == "": print('Invalid input!')
    elif nama in tinggiSiswa: print("Tinggi siswa tersebut adalah: %d cm" % tinggiSiswa[nama])
    else:
        print('Nama siswa '+nama+' belum ada di daftar data')
        newTinggi = int(input('Tinggi siswa: '))
        tinggiSiswa[nama] = newTinggi
        print('Database tinggi siswa telah diupdate')

# task 3
Harga_Buah = {'apel': 5500, 'manga': 9000, 'nanas': 10500, 'jambu':3000}
maxPrice = max(Harga_Buah, key=(lambda item: Harga_Buah[item])) #using anonymous function
minPrice = min(Harga_Buah, key=Harga_Buah.get)
print(maxPrice, Harga_Buah[maxPrice])
print(minPrice, Harga_Buah[minPrice])
