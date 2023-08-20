# episode 23
# latihan membuat kalkulator menggunakan artimatika,ifelse,dan kawan kawan nya


# kalkulator sederhana
print(20*"=")
print("selamat datang di kalkulator sederhana")
print(20*"=" +" \n")

angka_satu = float(input("masukan bilangan pertama : "))
operator = input("operator (+,-,*,/) : ")
angka_dua = float(input("masukan bilangan ke dua : "))

# percabangannya

if operator == "+":
  hasil = angka_satu + angka_dua
  print(f"hasilnya adalah {hasil}")

elif operator == "-":
  hasil = angka_satu - angka_dua
  print(f"hasilnya adalah {hasil}")

elif operator == "*" or operator == "x":
  hasil = angka_satu * angka_dua
  print(f"hasilnya adalah {hasil}")

elif operator == "/":
  hasil = angka_satu / angka_dua
  print(f"hasilnya adalah {hasil}")

else:
  print("input yang anda masukan salah")

print("SEKIAN TERIMA GAJI")




