# episode operator bitwase, operasi biner, binary

a = 9
b = 5

# biwase OR (|)
c = a | b #satu angka nilai nya 1 maka akan menghasilkan satu juga atau /+
print("\n===OR===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('nilai : ',b,'binernya adalah ;',format(b,'08b'))
print('------ (|) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))

# bitase AND (&)
c = a & b #harus memiliki 2 value yang 1 untuk mrndapatkan nilai 1 /x
print("\n===AND===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('nilai : ',b,'binernya adalah ;',format(b,'08b'))
print('------ (&) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))

# bitase XOR (^)
c = a ^ b #jika nilai sama" true maka akan menghasil kan false /0
print("\n===XOR===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('nilai : ',b,'binernya adalah ;',format(b,'08b'))
print('------ (^) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))

# bitwase NOT (~) sama dengan mirror
c = ~a
print("\n===NOT===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('------ (~) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))
#  akan di mirrpr ke negatif dengan selisih 1 dan tidak dimulai dari 0 (misal 9 menjadi -10)
print('--- (^) ---') #cara mengflip menjadi positif dengan xor
d = 0b0000001001
e = 0b1111111111
print('nilai : ',e^d,' ,binernya adalah : ',format(e^d,'08b'))


# shifting

# shif right (>>)
c = a >> 2
print("\n=== >> ===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('------ (>>) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))

# shif left (<<)
c = a << 2
print("\n=== << ===")
print('nilai : ',a,'binernya adalah ;',format(a,'08b'))
print('------ (<<) ------')
print('nilai : ',c,'binernya adalah ;',format(c,'08b'))