# operator dalam bentuk methods

# merubah case dari string

# merubah semua case ke upper

sapa = 'woi!'
print('normal : '+ sapa)
sapa = sapa.upper()
print('upper : '+ sapa)

# merubah semua ke lowwer case

anjay = 'SenGoL DoNg'
print('normal=' + anjay)
anjay = anjay.lower()
print('lower=' + anjay)

## pengceksn isX method

# contoh pengecekan lower case
salam = 'cok'
apakah_lower = salam.islower() #hasilnya boolean
print(salam + 'is lower :',apakah_lower)
apakah_upper = salam.isupper() 
print(salam + 'is upper :',apakah_upper)

# isalpha <-- untuk mengecek semuanya huruf
# isalnum <-- untuk mengecek huruf dan angka
# isdecimal <-- untuk mengecek number only
# isspace <-- spasi, tab, newlinr \n
# istitle <--semua kata di mulai dari huruf besar

user = 'hasan'
password = 'badiro12'
sandi = '2307'
namleng = 'Hasan Almunawar Ganteng Slebeww'



# isalpha
satu = user.isalpha()
print('isalpha' + str(satu))

# isalnum
dua = password.isalnum()
print('isalnum' + str(dua))

# isdecimal 
tiga = sandi.isdecimal()
print('isdecimal' + str(tiga))

# istitle 
empat = namleng.istitle()
print('istitile'+ str(empat))

## ngecek komponen dengan startswith() endwitdh() <-- keren
cek_starts = "sandeltod depol".startswith("san")
print('star = ' + str(cek_starts))

cek_end = "sandantod ngen".endswith("ngen")
print("end " + str(cek_end))

## penggabungan komponen join() split()

tele = ['aku', 'suka', 'mieAyam'] #list

gabung = " kiw ".join(tele)
print(gabung)

gabung = "akukiwsukakiwmieayam"
print(gabung.split('kiw'))

# alokasi karakter rjust() ljust() center()
print(5*"=" + "depol" + "="*5) # cara lama

kanan = "Judul".rjust(10,"=")
print("'" + kanan + "'")

print("data".rjust(10,"_"))

print("data".center(20,"="))

# kebalikan nya <-- strip()

kanan = kanan.strip("=") #mghilangkan tanda =
print(kanan)