a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
d = {a,b,c}
sortList = sorted(d)
print("Xep tang dan:",end = " ")
for x in range(len(sortList)):
    if x<len(sortList) -1: 
        print(sortList[x],end = " ")
    else:
        print(sortList[x])
    
