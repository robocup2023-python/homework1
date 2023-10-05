x,y,z=input("Please input three numbers,and I will sort them by size: ").split()   #list
if int(x)>int(y):
    x,y=y,x
if int(y)>int(z):
    y,z=z,y
    if int(x)>int(y):
        x,y=y,x
print(f"The result is:\n\t{x}\n\t{y}\n\t{z}")
