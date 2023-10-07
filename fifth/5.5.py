from pathlib import Path
from random import randint
def create_files(name):
    current_dir=Path(__file__).resolve()
    img_dir=current_dir / 'img'
    img_dir.mkdir(exist_ok=True)  #?
    count=0;list_of_random=[]
    while count<=99:
        a=randint(0,99)
        if a not in list_of_random:
            count+=1
            list_of_random.append(a)
            
    for i in range(1,101):
        suffix='txt'
        if i in list_of_random:
            suffix='png'

        file_name=f"file{i}"+suffix
        file_path=img_dir / file_name
        with open(file_path,'w') as file:
            file.write(f'This is file {i}')
    
