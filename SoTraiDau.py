def check(a,b,c):
    if a*b>0 and a*c>0 and b*c>0:
        return True
    return False

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Khong co cap so trai dau" if check(a,b,c) else "Co cap so trai dau")
