import pathlib
import random
import string

test_dir=pathlib.Path("./test")
test_dir.mkdir(exist_ok=True)
i=int(input("number of files: "))
j=int(input("lines of files: "))
for n in range(i):
    file_name=f'test/file{n}.txt'
    with open(file_name,"w") as f:
        for _ in range(j):
            line=''.join(random.choices(string.ascii_letters+string.digits,k=random.randint(1,50)))
            f.write(line+'\n')
for path in pathlib.Path("test").glob("*"):
    if path.is_file():
        new_name0="./test/"+path.stem+'-python'+path.suffix
        new_content=''
        path1=path.rename(new_name0)
        with open(path1,"r") as f:
            for line in f:
                new_content+=line.strip()+"-python\n"
        with open(path1,'w') as f:
            f.write(new_content)

        

