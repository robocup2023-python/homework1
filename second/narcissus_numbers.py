lists=[]
for i in range(100,1000,1):
    a,b,c=list(str(i))
    A,B,C=int(a),int(b),int(c)
    if A**3+B**3+C**3==i:
        lists.append(i)
print(lists)