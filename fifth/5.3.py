from random import randint as kd
def create_random_text():
    txt_file=open('data.txt','w',encoding='utf-8') #utf-8 w
    for i in range(100000):
        print(kd(1,100),file=txt_file)
    txt_file.close()
create_random_text()