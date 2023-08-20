import datetime
import os
import string
import random
# template mahasiswa
mahasiswa_template = {
  "nama" : "nama",
  "nim" : "87654321",
  "sks_lulus" : 0,
  "lahir" : datetime.datetime(1111,1,11)

}


data_mahasiswa = {}

while True:
    os.system("cls") #untuk windows
    # print(data_mahasiswa)
    # print(mahasiswa_template)
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama mahasiswa = ")
    mahasiswa['nim'] = input("Nim mahasiswa = ")
    mahasiswa['sks_lulus'] = int(input("Sks mahasiswa = "))

    TAHUN_LAHIR = int(input("Tahun lahir (YYYY):"))
    BULAN_LAHIR = int(input("Bulan lahir (1-12):"))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31):"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    # print(mahasiswa)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) #inti dari random

    data_mahasiswa.update({'KEY':mahasiswa})

    print(f"{'KEY':<6} {'NAMA':^17} {'NIM':^14} {'SKS LULUS':<12} {'TANGGAL LAHIR':<10}")
    print("-"*70)

    for mahasiwa in data_mahasiswa:
      KEY = mahasiwa

      NAMA = data_mahasiswa[KEY] ['nama']
      NIM = data_mahasiswa[KEY] ['nim']
      SKS = data_mahasiswa[KEY] ['sks_lulus']
      TTL = data_mahasiswa[KEY] ['lahir'].strftime('%x')
      

      print(f"{KEY:<6} {NAMA:^17} {NIM:^14} {SKS:^9} {TTL:^15}")
      
      print("\n")
    isDone = input("mau nambah lagi bro? (y/n)")
    if isDone == "n":
      break
print("\n akhir dari program ini, Terima kasih")


