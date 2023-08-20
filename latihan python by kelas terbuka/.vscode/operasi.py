# operasi logika atau boolean 

# not, or, and, xor

print('===NOT===')
a = False
c = not a
print('nilai a adalah', a)
print('===NOT===')
print('nilai c adalah', c)

print('===OR===') #ibaratkan seperti + (false = 0, true = >1)
a = False
b = False
c = a or b
print(a,'OR',b,'=', c) # 0 + 0 = =

a = False
b = True
c = a or b
print(a,'OR',b,'=', c) # 1 + 0 = 1

a = True
b = False
c = a or b
print(a,'OR',b,'=', c)

a = True
b = True
c = a or b
print(a,'OR',b,'=', c)

print('===AND===') #ibaratkan seperti * (false = 0, true = >1)
a = False
b = False
c = a and b
print(a,'AND',b,'=', c) 

a = False
b = True
c = a and b
print(a,'AND',b,'=', c) 

a = True #
b = False
c = a and b
print(a,'AND',b,'=', c) # 1 * 0 = 0 (false)

a = True
b = True
c = a and b
print(a,'AND',b,'=', c)  # 1 * 1 = 1 (true)



print('===XOR===')  #jika 2 buah variabel memiliki
# jika duah buah variabel memiliki nilai yang sama (tr+tr/fl+flmaka akan menjadi false
# sedangkan jika nilai berbeda maka akan menjadi true

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=', c) 

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=', c) 

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=', c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=', c)




