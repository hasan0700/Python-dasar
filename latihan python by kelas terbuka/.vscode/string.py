# penjelasan tentang string
# string memiliki beberapa type

print('halo apa kaba"r')
print("jangan lupa jum'atan ")
print('baris kesatu,\n baris kedua')
print('g\'day, isn\' it?')

# backlash
print("c:\\user\\engkos")

# tab
print('baris nge\t tab')

# backspash 
print("engkos \botong, jadi deketan")

# newLine
print("baris pertama.\nbaris kedua") #LF ->line head untuk unix, macos, linux
print("baris pertama.\rbaris kedua") #CR ->carriage untuk return commodore, acorn
print("baris pertama.\r\nbaris kedua") #CRLF -> line feed carriage return


# 3.string literal atau raw
# hati-hati
print('C:\\new folder') #akan salah pathny jika hanya menggunakan satu \

# menggunakan sedikit django(raw string)
print(r'C:\new folder')

# bisa pakai multyLine literal string
print("""
nama: hasan almunawar
kelas: sistem informasi
""")

# multyline literal string dan row
print(r""" 
nama : engkos
kelas : slebew
Website: www.engkos.com/newID\tabauki
""")








