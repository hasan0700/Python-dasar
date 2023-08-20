# operasi decnary

data_dict = {
  "cup" : "ucup surucup",
  "tong" : "otong surotong",
  "tid" : "titid suritid",

}

# mengambil panjang dari dicnary
LENDICT = len(data_dict)
print(f"panjang data dict: {LENDICT}")

# mengecek key exist atau tidak
KEY = "tid"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di dalam {CHECKKEY}")