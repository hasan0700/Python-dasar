# name = input("give your name in here : ")

# for alfa in name:
#   print(alfa)

# spam = range(100)

# for ongko in spam:
  # print(f"hayoooo ripper yaaaa {ongko}")


# listIn = list(input("masukan list = "))

# for huruf in listIn:
#   print(f"potongan {huruf}")

def read_ints(): return [int(x) for x in masuk().split()]

def cat(l): return tuple(sum(l[n::3]) for n in [1, 2, 0])


masuk = input("masukan:") # n
A = cat(read_ints())
B = cat(read_ints())
print("{} {} {}".format(B[2] * A[0] + B[0] * A[2] + B[1] * A[1],
    B[2] * A[1] + B[0] * A[0] + B[1] * A[2],
    B[2] * A[2] + B[0] * A[1] + B[1] * A[0]))

 
