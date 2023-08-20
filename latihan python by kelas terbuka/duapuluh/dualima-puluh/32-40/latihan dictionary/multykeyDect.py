import datetime

mahasiswa1 = {
  'nama': 'ucup maricup',
  'nim': '123456701',
  'sks_lulus':145,
  'beasiswa':True,
  'lahir' : datetime.datetime(2004,7,23)

}
mahasiswa2 = {
  'nama': 'otong marito',
  'nim': '123456702',
  'sks_lulus':145,
  'beasiswa':False,
  'lahir' : datetime.datetime(2000,2,29)

}
mahasiswa3 = {
  'nama': 'fulan landio',
  'nim': '123456703',
  'sks_lulus':145,
  'beasiswa':False,
  'lahir' : datetime.datetime(1999,4,24)

}

data_mahasiswa = {
  "MAH01" : mahasiswa1,
  "MAH02" : mahasiswa2,
  "MAH03" : mahasiswa3,
}

print(f"{'KEY':<6} {'NAMA':^17} {'NIM':^14} {'SKS LULUS':<12} {'BEASISWA':<8} {'TTL': ^10}")
print("-"*80)

for mahasiwa in data_mahasiswa:
  KEY = mahasiwa

  NAMA = data_mahasiswa[KEY] ['nama']
  NIM = data_mahasiswa[KEY] ['nim']
  SKS = data_mahasiswa[KEY] ['sks_lulus']
  BEASISWA = data_mahasiswa[KEY] ['beasiswa']
  TTL = data_mahasiswa[KEY] ['lahir'].strftime('%x')
  

  print(f"{KEY:<6} {NAMA:^17} {NIM:^14} {SKS:^9}  {BEASISWA:8} {TTL: ^10}")
  # print(f"{KEY:<6} {NAMA:<17} {NIM:^14} {SKS:^9} {PRODI:<10} {BEASISWA:^8} {TTL: <10}")

# print(TTL)