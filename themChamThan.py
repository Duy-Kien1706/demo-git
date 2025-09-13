s = input("Nhap S: ")
if s.endswith("!!!"):
    s+=""
elif s.endswith("!!"):
    s+="!"
elif s.endswith("!"):
    s+="!!"
else:
    s+="!!!"
print("Chuoi S sau khi xu ly:",s)