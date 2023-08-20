data0 = [1,2,3,4]
data1 = [5,6,7]


data2d = [data0,data1, 10]
data2d_copy = data2d.copy()
print(f"ini adalah data gabungan = {data2d}")

# ingin mengambil sebuah data

dataAmbil = data2d[0][1]
print(f"data yang di ambil = {dataAmbil}")

# cek addres
print(f"cek addres asli {hex(id(data2d))}")
print(f"cek addres copy {hex(id(data2d_copy))}")

print("\n addres dari member 1")
print(f"cek addres asli {hex(id(data2d[0]))}")
print(f"cek addres copy {hex(id(data2d_copy[0]))}")



dataAmbil = data2d[0][1] = 5
data2d[2] = 9
print(f"data asli {data2d}")
print(f"data copy { data2d_copy}")


# menggunakan deep copy

from copy import deepcopy
data2d = [data0, data1, 10]
dataNew2 = deepcopy(data2d)

print(dataNew2)


print("\n addres dari member 1 setelah di deepcopy")
print(f"cek addres asli {hex(id(data2d[0]))}")
print(f"cek addres copy {hex(id(dataNew2[0]))}")


dataAmbil = data2d[0][1] = 12
print(f"data = {data2d}")
print(f"data deep = {dataNew2}")