def themN23(n,x,i,d):
    while(len(d) < n):
        if 2* d[i]+ 1 < 3*d[x] +1:
            d.append(2*d[i]+1)
            i+=1
        elif 2*d[i]+1 > 3*d[x]+1:
            d.append(3*d[x]+1)
            x+=1
        else:
            d.append(3*d[x]+1)
            i+=1
            x+=1
    return d

n = int(input("N = "))
i = 0
x = 0
d = [1]
print(f"{len(themN23(n, x, i, d))} so dau tien cua N23:",end = " ")
for i in range(len(themN23(n, x, i, d))):
    if i< len(themN23(n, x, i, d)) -1 :
        print(themN23(n, x, i, d)[i],end = " ")
    else:
        print(themN23(n, x, i, d)[i])