# # latihan membuat ketupat menggunakan looping


# # count = 1
# # while True:
# #   print("*"*count)
# #   count += 1

# #   if count > sisi:
# #     break

# sisi = 10


# count = 1
# spashi = int(sisi / 2)
# while True:
#   if count % 2 :
#     print(" "*spashi,"*"*count)
#     spashi -= 1
#     count += 1

#   else :
#     count += 1
#     continue
#   if count > sisi:
#     break 


# while True:
#   if count % 2:
#     spashi += 1
#     print(" "*spashi,"*"*count)
#     count -= 1
  
#   else :
#     count -= 1
#     continue

#   if count == 0:
#     break

sisi = 1
for i in range(sisi):
  print("*"*10)
  sisi += 1