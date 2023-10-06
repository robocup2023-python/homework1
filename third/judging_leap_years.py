year=int(input())
if year%400==0:
    print("%d is the century leap years."%(year))
elif year%4==0:
    print(f"{year} is the ordinary leap years.")
else:
    print('no')