import random
n=int(input('n: '))
m=int(input('m: '))
lists=[]
for i in range(n):
    lists.append(random.randint(1,100))
print(lists)
for i in range(m):
    lists.insert(0,lists.pop())
print(lists)