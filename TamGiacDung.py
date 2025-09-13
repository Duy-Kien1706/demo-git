def check(a,b,c):
    if a>0 and b>0 and c>0:
        return True if a+b>c and a+c>b and b+c>a else False
    else:
        return False
    
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Dung la tam giac" if check(a,b,c) else "Khong phai tam giac")


