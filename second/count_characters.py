lists_c=input("Please input a line of characters: ")
Eng=0;num=0;spa=0;oth=0
for i in lists_c:
    if i.isalpha():
        Eng+=1
    elif i.isdigit():
        num+=1
    elif i ==" ":
        spa+=1
    else:
        oth+=1
print(Eng," ",spa," " ,num," ",oth)
