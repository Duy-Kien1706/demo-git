def tongS(s):
    tong =0
    while s>0:
        tong+=s%10
        s//=10
    return tong

n = int(input("N = "))
s = 2**n
print("Tong =",tongS(s))

