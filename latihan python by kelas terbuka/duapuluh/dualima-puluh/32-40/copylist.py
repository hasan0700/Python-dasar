# teknik menduplikat list

a = ["ucup", "dudung", "totong","olong"]

print(f"a = {a}")

b = a  #pass by refrence

print(f" b = {b}")

# kita akan merubah member dari a


# ini akan merubah kedua list
a[0] = "micheal"

b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list

# print(f"addres a = {hex(id(a))}")
# print(f"addres b = {hex(id(b))}")


# membuat list c dengan a.copy

c = a.copy() #full duplicate / membuat addres baru

print(f"addres c = {hex(id(c))}")

c[0] = "tonil"

print(f"c = {c}")


c.remove("olong")


print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"c = {c}")
