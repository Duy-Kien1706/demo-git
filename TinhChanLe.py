def check(a,b,c):
    return a%2==b%2==c%2


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
print("Cung tinh chan le" if check(a,b,c) else "Khac tinh chan le")        
