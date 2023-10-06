a=input("please input the 'a': ")
num=input("please input the numbers: ")
amount=0
for i in range(int(num)):
    amount+=int(a*(i+1))
print(f"\nthe answer is {amount}")

