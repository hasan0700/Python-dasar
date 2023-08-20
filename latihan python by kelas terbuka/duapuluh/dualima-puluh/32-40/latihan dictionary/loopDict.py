# melooping dict

myFrends = {
  "cup":"ucup maricup bagincup",
  "tong":"otong mritong begintong",
  "san":"marisan sonan nangsan",
  "dung":"dudung maridung markafung",
  }

# looping first try(mengambil key)

for frend in myFrends:
  print(frend)

# melooping untuk mengambil items /iterables
print("\n")
# keys = myFrends.keys()
# print(keys)

for kawan in myFrends.keys():
  print(myFrends.get(kawan))

print("\n")
# values = myFrends.values()
# print(values)

for value in myFrends.values():
  print(value)

print("\n")
item = myFrends.items()
print(item)

for valu in myFrends.items():
  print(valu)

print("\n")
for keys,values in myFrends.items():
  print(f"key={keys}, values= {values}")
  

