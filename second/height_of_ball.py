length=0
original_height=100
lists=[100]
for i in range(9):
    lists.append(lists[-1]*0.5)
for i in range(len(lists)):
    c=2
    if i==0:
        c-=1
    length+=lists[i]*c
tall=lists[-1]*0.5
print(round(length,3),round(tall,4))






