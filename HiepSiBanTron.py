def Find(n):
    a = [x for x in range(1,n+1)]
    i = 0
    while len(a)>1:
        i = (i+2)%len(a)
        a.pop(i)
    return a[0]
n = int(input("So nguoi ngoi quanh ban: "))
print("Nguoi o lai cuoi cung la nguoi thu",Find(n))


