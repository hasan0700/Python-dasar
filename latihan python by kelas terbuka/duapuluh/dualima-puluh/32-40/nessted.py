# nested list

data0 = [0,1,2,3]
data1 = [4,5,6,7,8]

listBiasa = [1,2,3,4,5,6,7]

print(f"list biasa = {listBiasa}")

# menggabungkan 2 list

list2D = [data0,data1]

print(f"ini list 2D = {list2D}")

# contoh penggunaan 
peserta1 = ["hasan", 21, "laki-laki"]
peserta2 = ["almu", 32, "laki-laki"]
peserta3 = ["depoll", 21, "ciwi"]

daftarPeserta = [peserta1, peserta2, peserta3]

print(f"daftar peserta ={daftarPeserta}")

for peserta in daftarPeserta:
  print(f"nama = {peserta[0]}")
  print(f"umur = {peserta[1]}")
  print(f"kelamin = {peserta[2]} \n")

# with refrence

daftarCopy = daftarPeserta.copy()

print(f"ini adalah copyan = {daftarCopy}")

peserta1[0] = "michel"

print(f"ini adalah ubahan = {daftarCopy}")
print(daftarPeserta)