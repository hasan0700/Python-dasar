# latihan looping
# membuat segitiga menggunakan looping
# menggunakan for

sisi = 12
# sisi = int(input("input number : "))


#1. membuat segitiga menggunakan for
# print("program awal")

# count = 1
# for i in range(sisi):
#   print("*"*count)
#   count += 1

# print("program akhit \n")

#2. membuat program menggunakan while
print("program awal while")
count = 1
while True:
  print("*"*count)
  count += 1

  if count > sisi:
    break

print("program akhir while\n")


# 3.hanya ganjil saja
print("program awal while ganjil")
count = 1
while True:
  # akan kembali ke atas jika ganjil
  if count % 2 :
    # akan print jika ganjil
     print("*"*count)
     count += 1

  else: #akan break jika atas jika ganjil
    count += 1
    continue


  # akan print jika count melebihi sisi 
  if count > sisi:
    break

print("program akhir while ganjil\n")


# 4. membuat segitiga sama kaki
print("program awal while ganjil")
count = 1
spashi = int(sisi / 2)
while True:
  # akan kembali ke atas jika ganjil
  if count % 2 :
    # akan print jika ganjil
     print(" "* spashi,"+"*count)
     spashi -= 1
     count += 1

  else: #akan break jika atas jika ganjil
    count += 1
    continue


  # akan print jika count melebihi sisi 
  if count > sisi:
    break

print("program akhir while ganjil\n")

