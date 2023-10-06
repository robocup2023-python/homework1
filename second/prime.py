def isprime(a):
    otm=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            otm=False
    return otm

for i in range(101,201,1):
    if isprime(i):
        print(i,end=" ")