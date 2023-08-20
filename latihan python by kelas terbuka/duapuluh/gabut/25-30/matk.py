# latihan coding bareng dea part 1

# kecepatan = jarak x waktu
# luas segitiga = 1/2 x a x t
# luas balok = 2pl + 2pt + 2lt
# luas bola = 4 x phi x r2

# import os  #berguna untuk mengclear ketika ingin memilih lagi

def hitung_kecepatan():
    print("hitung kecepatan ready!")
    jarak = float(input("masukan jarak : "))
    waktu = float(input("masukan waktu : "))
    kecepatan = jarak * waktu
    print(f"kecepatan : {kecepatan} \n")

def hitung_luasSegitiga():
    print("hitung luas Segitiga ready!")
    alas = float(input("masukan alas : "))
    tinggi = float(input("masukan tinggi : "))
    luasSegitiga = 1/2 * (alas * tinggi)
    print(f"Luas Segitiga : {luasSegitiga} \n")

def hitung_luasBalok():
    print("hitung luas Balok ready!")
    panjang = float(input("masukan panjang : "))
    lebar = float(input("masukan lebar : "))
    tinggi = float(input("masukan tinggi : "))
    luasBalok = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print(f"Luas Balok : {luasBalok} \n")

def hitung_luasBola():
    print("hitung luas Bola ready!")
    r = float(input("masukan jari jari : "))
    luasBola = 4 * 3.14 * (r**2)
    print(f"Luas Bola : {luasBola} \n")




while True:
  userInput = int(input("pilih rumus yang ingin di gunakan : \n1.keceptan \n2.luas segitiga \n3.luas balok \n4.luas bola \n0.keluar program \n pilih no berapa : " ))
  # os.sydtem('clear')
  if userInput == 1:
    hitung_kecepatan()
  elif userInput == 2:
    hitung_luasSegitiga()
  elif userInput == 3:
    hitung_luasBalok()
  elif userInput == 4:
    hitung_luasBola()
  else:
    break
  