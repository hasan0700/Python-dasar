# operasi komperasi

# setiap hasil dari operasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2


#  lebih besar dari >
print('======== lebih besar ======(>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

#   kurang dari <
print('======== kurang dari ======(<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

#  lebih dari sama dengan  >=
print('======== lebih dari sama dengan ======(>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

#  kurang dari sama dengan <= 
print('======== kurang dari sama dengan ======(<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan ==
print('========  sama dengan ======(==)')
hasil = a == 4
print(a, '==', 4,'=',hasil)
hasil = b == 4
print(b, '==', 4,'=',hasil)

# tidak sama dengan !=
print('========  sama dengan ======(!=)')
hasil = a != 4
print(a, '!=', 4,'=',hasil)
hasil = b != 4
print(b, '!=', 4,'=',hasil)

# 'is' sebagai komperasi object indectity
print('========  object identity ======(is)')
x = 5 #ini adalah assigment
y = 5
print('nilai x adalah',x,'id =', hex(id(x)))
print('nilai y adalah',y,'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 #ini adalah assigment
y = 6
print('nilai x adalah',x,'id =', hex(id(x)))
print('nilai y adalah',y,'id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is' sebagai komperasi object indectity
print('========  object identity ======(is not)')
x = 5 #ini adalah assigment
y = 5
print('nilai x adalah',x,'id =', hex(id(x)))
print('nilai y adalah',y,'id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5 #ini adalah assigment
y = 6
print('nilai x adalah',x,'id =', hex(id(x)))
print('nilai y adalah',y,'id =', hex(id(y)))
hasil = x is not y
print('x is not  y =', hasil)