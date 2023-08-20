# format string 

# contoh generic
# string
nama = "hasan"
# str = "hello " + nama
# print(str)

# menggunakan format
format_str = f"hello {nama}"
print(format_str)

# boolean 
bole = False
format_bol = f"bolrean = {bole}"
print(format_bol)

# angka
angka = 2004.5
format_angka = f"angka = {angka}"
print(format_angka)

# bilangan bulat
bulat = 15
format_bulat = f"bilangn bulat = {bulat:d}" # d= desimal
print(format_bulat)

# bilanga ordo ribuan atau jutaan
ribu = 200000
format_ribu = f"bilangan ribu = {ribu:,}" # kome(,) berati penanda ribuan atau lebih
print(format_ribu)

# bilangan desimal
angka = 2004.54321
format_str = f"desimal = {angka:.2f}" #float menandakan bahwa di ambil dari belakang sebelom koma
print(format_str)

# menampilkan leading zero
angka = 2004.54321
format_angka = f"desimal = {angka:08.2f}"
print(format_angka)

# menampilkan tanda - dan +
angak_min = -10
angka_plus = +10.1234
format_min = f"angka minus = {angak_min:+d}"
format_plus = f"angka plus = {angka_plus:+.2f}"

print(format_plus)
print(format_min)

# mengfirmat persen 
persentase = 0.045
format_persentase = f"persen = {persentase:.2%}"
print(format_persentase)

# melakukan operasi aritmatika di dalam plase holder
harga = 10000
jumlah = 5

format_bayar = f"harga total =rp. {harga*jumlah:,}"
print(format_bayar)

# format angka (binary, octal, hex)

angka = 255

format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

