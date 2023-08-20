# mengcopy dict

myFrends = {
  "cup":"ucup maricup bagincup",
  "tong":"otong mritong begintong",
  "san":"marisan sonan nangsan",
  "dung":"dudung maridung markafung",
  }

print("COPYAN BIASA")
temanKU = myFrends
print(f"my frends = {myFrends} \n")
print(f"temak ku = {temanKU}\n")



print("PRAKTEK UBAH ISI COPYAN")
myFrends["cup"] = "tongmalaotng"
print(f"my frends = {myFrends} \n")
print(f"temak ku = {temanKU}\n")


# cara mengcopy dengan benar
print("MENGCOPY DENGAN BENARRR")
temanHasan = myFrends.copy()
myFrends["san"]="engkosss"

print(f"teman hasan = {temanHasan}\n")
print(f"my frends = {myFrends} \n")

# mengambil data dengan pop (pop adalah mengambil data menjadi keluar)
dataSan = temanHasan.pop("san")
print(f"dataSan adalah {dataSan}\n" )
print(f"teman hasan = {temanHasan}\n")

# popItem dict (mengambil data yang paling akhir)
dataLet = temanHasan.popitem()
print(f"dataSan adalah {dataLet}\n" )
print(f"teman hasan = {temanHasan}\n")