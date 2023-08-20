#  perulangan (loop)

# for kondisi
#  aksi


# perumpamaan 
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)


# with list
angka_list = [0,2,4,6,8,10] #ini adalah list
print(angka_list ,"\n")

for i in angka_list:
  print(f"i sekaragn adlah {i}")

print("ini adalah akhir dari program 1 ","\n")

# with range
angka_range = range(1,5) #jika menggunkan koma maka akan di baca satu sampai 5 
                        #normal nya menggunakan (5,dst)
for i in angka_range:
  print(f"i sekaragn adlah {i}") #selalu di mulai dari nol
  
print("ini adalah akhir dari program 2 ","\n")

for i in angka_range:
  print("aku keren abiss") 
  
print("ini adalah akhir dari program 3 ","\n")

# with string
data_str = "aku ganteng anjayy"

for huruf in data_str:
  print(huruf)

print("ini adalah akhir dari program 4 ","\n")


