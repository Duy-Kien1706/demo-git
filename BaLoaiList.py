def checkInt(x):
    try:
        int(x)
        return True
    except:
        return False

def checkFloat(x):
    try:
        float(x)
        return True
    except:
        return False


def check(n,a,b,c):
    for i in range(n):
        value = input(f"Nhap gia tri thu {i+1}: ")
        if(checkInt(value)):
            a.append(int(value))
        elif(checkFloat(value)):
            b.append(float(value))
        else:
            c.append(value)
            
n = int(input("Nhap N: "))
a = []
b = []
c= []
check(n,a,b,c)
a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)
print("A =",a)
print("B =",b)
print("C =",c)