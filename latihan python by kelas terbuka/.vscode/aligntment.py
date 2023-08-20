#  width and multiline

# Data 
data_nama = "hasan almunawar"
data_umur = 18
data_tinggi = 171.1
data_sepatu = 44

# string standart
data_string = f"nama ={data_nama}, umur ={data_umur}, tinggi={data_tinggi}, sepatu ={data_sepatu}"
print(5*"="+"Data string"+"="*5)
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama ={data_nama}, \numur ={data_umur}, \ntinggi={data_tinggi}, \nsepatu ={data_sepatu}"
print("\n"+5*"="+"Data string"+"="*5)
print(data_string)

# string multiline(kutip triples)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_sepatu}


""" #menampilkan sesuai dengan apa yang di ketik
print("\n"+5*"="+"Data string"+"="*5)
print(data_string)

# mengatur lebar 
data_nama = "hasan"
data_string = f"""
nama    = {data_nama}
umur    = {data_umur:>5}
tinggi  = {data_tinggi}
sepatu  = {data_sepatu:>5} 

""" # (.>) digunakan untuk menggeser jadi rata kanan
print("\n"+5*"="+"Data string"+"="*5)
print(data_string)

