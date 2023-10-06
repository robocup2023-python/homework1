a=input("input year,month,day,using ',' to seperate them: ").replace(" ","").split(',')
year=int(a[0]);month=int(a[1]);day=int(a[2])
month_day={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,12:31,11:30}
if year%4==0:
    month_day[2]=29
count=0
for i in range(1,month):
    count+=month_day[i]
count+=day
print(count)