a=list(map(int,input("X= ").replace('\n','').replace("[",'').replace(']','').split(',')))
b=list(map(int,input("Y= ").replace('\n','').replace("[",'').replace(']','').split(',')))
print('X+Y= ')

count=0
lists=[]
for i in range(len(a)):
    count+=1
    lists.append(a[i]+b[i])
    if count==3:
        print (lists)
        lists=[]
        count=0
    

