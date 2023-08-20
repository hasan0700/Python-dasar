# LIST

# list berisi number
list_num = [0, 1, 2, 3, 4, 5]
print(list_num)

# list menggunakan string
list_str = ["san", "nel", "tong"]
print(list_str)

# list berisi boolean
list_bool = [True, False, True, False]
print(list_bool)

# list berisi campuran
list_camp = [1, "nasi uduk", 2, "pihang goheng", True]
print(list_camp)

# alternatif membuat list
data_range = range(0,10,2) #range (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)


# membuat list menggunanakn for loop, list compresion
list_for = [i**2 for i in range(0,10)]
print(list_for)

list_forif = [i for i in range(0,10) if i != 5] #contoh menghilangkan angka 5
print(list_forif)

list_forif = [ i for i in range(0,10) if i % 2 ==0 ]
print(list_forif)

list_forif = [ i for i in range(0,10) if i % 2 != 0 ]
print(list_forif)