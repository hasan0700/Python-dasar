# mencari solusi untuk kasus irisan ke 2

# soal pertama ---0+++5---8+++11---
inputUser = float(input('masukan angka: '))

# ---0+++
positifSatu = (inputUser > 0)
print('angka bersifat: ',positifSatu)

# +++5---
positifDua = (inputUser < 5)
print('angka bersifat: ',positifDua)

isKoreksi = positifSatu and positifDua
print('angka memiliki nilai:',isKoreksi)


inputUser = float(input('masukan angka : '))
# ---8+++
positifTiga = (inputUser > 8)
print('angka bersifat: ',positifTiga)

# +++11---
positifEmpat = (inputUser < 11)
print('angka bersifat: ',positifEmpat)

isKoreks = positifEmpat or positifTiga
print('angka memiliki nilai:',isKoreks)

newKorek = isKoreksi ^ isKoreks
print('hasil akhirnya adalah : ',newKorek)
