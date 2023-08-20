# episode latihan logika dan lomperasi

# membuat gabungan area rentang dari angka

# +++3------10++++

inputUser = float(input('masukan angka yang bernilai kurang dari 3 \n atau \n lebih dari 10 : '))

# +++3
isKurangDari = (inputUser < 3)
print('kurang dari 3',isKurangDari)

# 10+++
isLebihDari = (inputUser > 10)
print('lebih dari 10', isLebihDari)

# +++3------10++++
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan bersifat',isCorrect)


#  -------3++++++++10------
# kasus irisan
print('\n',"="*10,'\n')
inputUser = float(input('masukan angka yang bernilai lebih dari 3 \n dan \n kurang dari 10 : '))

# ---3+++
isLebihDari = (inputUser > 3)
print('lebih dari 3',isLebihDari)

# ++++10-----
isKurangDari = (inputUser < 10)
print('kurang dari 10',isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukan bersifat',isCorrect)
























