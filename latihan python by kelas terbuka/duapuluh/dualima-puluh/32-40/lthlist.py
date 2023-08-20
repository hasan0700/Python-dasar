# ingin membuat daftar perpustakan menggunakan list

list_book = []
 

while True:
    print("MASUKAN DATA BUKU")
    judul = input("masukan judul buku \t: ")
    penulis = input("nama penulis buku \t: ")

    newDate = [judul, penulis]
    list_book.append(newDate)

    print("="*10,"DAFTAR BUKU","="*10)
    

    for index,buku in enumerate(list_book):
      print(f"{index+1} | {buku[0]}\t| {buku[1]}")


    finish = input("Do you want continues?\n(y/g) ")
    
    if finish == "g":
        break

    
