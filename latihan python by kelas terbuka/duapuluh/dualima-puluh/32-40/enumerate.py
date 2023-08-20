# loopig dari list

# for loop 
print("\nfor loop ")
groupNum = [4,3,2,1]

for num in groupNum:

   print(f"angka ke {num}")

peserta = ["ucup", "dadamg", "edoson"]

for nama  in peserta:
  print(f"nama = {nama}")

# for loop dan range 
print("\nfor loop range")

kumpulanAngka = [10, 1, 2,4,6,2]

panjang = len(kumpulanAngka)
for i in range(panjang):
  print(f"angka = {kumpulanAngka[i]}")

angkaKuadrat = [i**2 for i in kumpulanAngka]
print(angkaKuadrat)

# use while
print("\nwhile")

kumpulanAngka = [10, 1, 2,4,6,2]

panjang = len(kumpulanAngka)

i = 0

while i < panjang:
  print(f"angka = {kumpulanAngka[i]}")
  i += 1


# list comperesion
print("\n list comperesion")
data = ["ucup", 1,2,3,4, "dadang"]

[print(f"angka {i}") for i in data]


# enumarete
print('\n enumarete')
isi = ["ucup", 1,2,3,4, "dadang"]

for i,data in enumerate(isi):
  print(f"index = {i},data = {data}")
