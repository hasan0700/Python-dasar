# operator untul dictinary

data_dict = {
  "cup" : "ucup marucup",
  "ber" : "barlet surelet",
  "tod" : "tod marotod",

}

# panjang dictionary 
LENDICT = len(data_dict)
print(f"panjang dictionary {LENDICT}")

# mengecek keys exist ada atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah ada {KEY} nya? {CHECKKEY}") #hasil nya berupa boolean

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("lol","ndak ado peler")) #chek key dengan masage


# mengupdate data
data_dict["cup"] = ["markicup slebewww"]
print(data_dict,"\n")
data_dict["sep"] = "asep ksep pisan"
print(data_dict,"\n")

data_dict.update({"cup":"ucup markitong"})
print(data_dict,"\n")
data_dict.update({"san": "hasan almunawar bagiwaer"})
print(data_dict,"\n")

# mendelete data pada dictionary
del data_dict["san"]
print(data_dict,"\n")