def nhapGiaBan():
    d = {}
    print("NHAP BANG GIA:")
    while True:
        ten = input("  Ten mat hang: ")
        if ten == "":
            break
        gia = float(input("  Gia ban hang: "))
        d[ten] = gia
    return d

def nhapSoLuong():
    d = {}
    print("NHAP HANG TON:")
    while True:
        ten = input("  Ten mat hang: ")
        if ten == "":
            break
        ton = float(input("  So luong ton kho: "))
        d[ten] = ton
    return d
        
gia = nhapGiaBan()
tonKho = nhapSoLuong()
d = {}
print("THONG KE HANG TON:")
for x in gia:
    if x in tonKho:
        d[x] = gia[x]*tonKho[x]
    else:
        d[x] = 0.00
max_len = max(len(x) for x in d)
d = dict(sorted(d.items(),key = lambda x : (-x[1],x[0])))
for x in d:
    print(f"  {x.ljust(max_len)} {d[x]:6.2f}")