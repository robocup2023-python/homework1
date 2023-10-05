lists=[]
a=1;b=1
count=2
lists+=[a,b]
while count<20:
    c=a+b
    b=a
    a=c
    count+=1
    lists.append(c)
for i in range(len(lists)):
    print(lists[i],end=' ')
