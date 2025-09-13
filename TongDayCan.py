def tinhTong(n):
    tong = 0
    tong_can = 0.0
    for i in range(1,n+1):
        tong+=i
        tong_can+=tong**0.5
    return tong_can


n = int(input("N = "))
print("F(%d) = %.7f" %(n,tinhTong(n)))