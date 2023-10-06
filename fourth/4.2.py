a=[1,3,5,7,9,11]
b=int(input())
if b>a[-1]:
    a.append(b)
else:
    i=0
    while b>a[i]:
        i+=1
    a.insert(i,b) 
print(a)