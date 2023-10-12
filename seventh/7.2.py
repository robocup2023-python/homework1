from random import randint
def copy_files():
    i_=int(input())
    with open("test.txt",'w') as f:
        for i in range(i_):
            f.write(f'{chr(randint(32,127))}\n')
    with open("copy_test.txt","w") as cf:
        with open("test.txt") as f:
            content=f.read()
        cf.write(content)
copy_files()
    