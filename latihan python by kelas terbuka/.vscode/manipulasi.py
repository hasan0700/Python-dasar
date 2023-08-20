# operasi dan manipulasi string

# 1. menyambung string
nama_awal = "hasan"
nama_tengah = "al"
nama_akhir = "munawar"


nama_lengkap = nama_awal + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string menggunakan len
panjang = len(nama_lengkap)
print(panjang)

# 3.operator untuk string

# mengecek apakah ada komponen char atau string di string

h = "h"
status = h in nama_lengkap
print( h + " "+ "ada di" + nama_lengkap + " = " + str(status))

H = "H"
status = H in nama_lengkap
print( H + " "+ "ada di" + nama_lengkap + " = " + str(status))

h = "h"
status = h not in nama_lengkap
print( h + " "+ "ada di" + nama_lengkap + " = " + str(status))


# mengulang string
print('wk'*15)
print(15*'ha')

# indexing 
# semua di mulai dari 0
print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[1])
print("index ke-0 : " + nama_lengkap[4])
print("index ke-0 : " + nama_lengkap[-1]) # jika mines maka akan di ambil dari huruf di belakang
print("index ke-0 : " + nama_lengkap[1:5]) 
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:10:2]) # artinya index 0 sampai 10 namun di loncatin sebanyak 2buah


# item paling kecil
print('nilai paling kecil : ' + min(nama_lengkap)) #kosong krena paling nilai paling min adalah spashi

# item paling besar
print('nilai paling besar : ' + max(nama_lengkap))

ascii_code = ord("'")
print("ascii untuk ascii_code adalah : " + str(ascii_code))
data = 117 
print("char untuk ARCII 117  adalah : " + chr(data))


# 4.operator dalam bentuk method

data = "otong saratong martong"
jumlah = data.count("o")
print("jumlah o pada" + data + '='+ str(jumlah))


