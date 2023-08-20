data_angka = [1,2,3,4,2,4,6,2,7,0,]

print(f"data ny = \n{data_angka}")

# count data

jumlah4 = data_angka.count(4)
jumlah2 = data_angka.count(2)

print(f"jumlah 4 ada = {jumlah4}")
print(f"jumlah 2 ada = {jumlah2}")


# ambil posisi data(index)
data_nama = ["ucup","tolil","totong","engkos","kuntul"]

posisi = data_nama.index("totong")

print(f"index totong adalah {posisi}")


# mengurutkan list
print(f"sebelum di urutkan {data_angka}")
data_angka.sort()
print(f"sesduah di urutkan = \n {data_angka}")
data_nama.sort()
print(f"urutan nama adalah = \n {data_nama}")

# balik liat nya
data_angka.reverse()
print(f"sesduah di balik = \n {data_angka}")

data_nama.reverse()
print(f"urutan nama di balik adalah = \n {data_nama}")

