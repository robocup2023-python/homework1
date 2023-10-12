from random import randint
def create_file(name="robocup7.1"):
    with open(name,'w') as file:
        for i in range(10):
            for j in range(3):
                a=randint(1,1000)
                file.write(f"{a}")
                if j!=2:
                    file.write(",")
            file.write('\n')
def read_file(name='robocup7.1'):
    with open(name) as file:
        lists=file.readlines()
    new_list=lists[1].rstrip('\n')#.split(',')
    new_list1=new_list.split(',')
    new_list2=[]
    for i in new_list1:
        new_list2.append(int(i))
    maxi=max(new_list2);mini=min(new_list2);aver=sum(new_list2)/len(new_list2)
    new_list2.remove(maxi)
    new_list2.remove(mini)
    mid=new_list2.pop()
    return maxi,mini,aver,mid

        

            
