count=0
lists=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                count+=1
                lists.append(i*100+j*10+k)
print(f"there are {count} numbers eligible\n")
print("they are:")
for i in range(len(lists)):
    print( f"\t{lists[i]}")
