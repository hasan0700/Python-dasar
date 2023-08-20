# operasi

# index  0(-3)  1(-2)     2(-1)
data = ["ucup", "otong", "dudung"]

# menganbil data dari list 
data_0 = data[0]
print((data_0))

data_terakhir = data[-1]
print(data_terakhir)

# mengambil info jumlah data yang ada di list
panjang = len(data)
print(f"panjang data adalah {panjang}")


## manipulasi data list

# menambah item ke dalam list sesuai posisi

print(f"data sebelum di tambah =\n {data}")

data.insert(1, "hasan")  #data.insert(posisi, item)
print(f"data sesudah di tambah = \n {data}")

# menambah data list di akhir
data.append("jojong")
print(f"setelah di tambah di akhir= \n{data}")

# menggabung kan 2 list
newData = ["sepol", "jhon", "sugiono"]
data.extend(newData)
print(f"setelah di gabung = \n{data}")

## merubah data

# mengubah data ke2(otong) menjadi joni
data[2] = "joni"
print(f"setelah di rubah = \n{data}")

# menghapus data
data.remove("joni") #akan error jika huruf tidak sesuai dengan yang ada di list
print(f"setelah di hapus = \n{data}")


# meremove data yang paling akhir
dataAkhir = data.pop()
print(f"hapus data akhir = \n{data}")

print(dataAkhir)