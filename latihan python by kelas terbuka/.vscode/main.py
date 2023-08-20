# kita belajar casting
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, bool 

print("===INTERGER===")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))


data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool)) #akan menjadi false jika bilangan int = 0

print("===FLOAT===")
data_float = 9.9; 
print("data = ", data_float, ",type =",type(data_float))


data_int = int(data_float) #akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai floar = 0
print("data = ", data_int, ",type =",type(data_int)) 
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

print("===STRING===")
data_str = "20"
print("data = ", data_str, ",type =",type(data_str))


data_float = float(data_str) #str harus angka
data_int = int(data_str) #str harus angka
data_bool = bool(data_str) #false jika str kosong
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_bool, ",type =",type(data_bool))

print("===BOOLEAN===")
data_bool = True;
print("data = ", data_bool, ",type =",type(data_bool))


data_float = float(data_bool)
data_str = str(data_bool)
data_int = int(data_bool)
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_int, ",type =",type(data_int))
