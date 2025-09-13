def tongUoc(n):
    tong = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            tong+=i
            if i != n//i:
                tong+= n//i
    return tong
            
n = int(input("N = "))
print(f"Tong cac uoc so cua {n} la {tongUoc(n)}"