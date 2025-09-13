def check(n):
    a = 0
    b = 1
    while b<n:
        a,b=b,a+b
    return b==n

#code
n = int(input("N = "))
if check(n) and n%2==0:
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")
