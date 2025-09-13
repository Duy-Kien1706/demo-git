'''
def tinhTong(n):
    if n==0:
        return 0
    return n+tinhTong(n-1)
def tongCan(n):
    if n==1:
        return 1
    return tinhTong(n)**(1/n) + tongCan(n-1)
'''
n= int(input("N = "))

tong = 0
tongCan = 0.0
for i in range(1,n+1):
    tong+=i
    tongCan += tong**(1/i)

print("F(%d) = %.7f" %(n,tongCan))
