n = int(input("Nhap N: "))
a = []
b = []
for i in range(1,n+1):
    value = input(f"Nhap gia tri thu {i}: ")
    try:
        a.append(float(value))
    except:
        b.append(value)
if len(a)>0:
    print("TBC cua A =",sum(a)/len(a))
print("B =",b)        