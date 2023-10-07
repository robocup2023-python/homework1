from pathlib import Path
def create_files(name):
    current_dir=Path(__file__).resolve()
    img_dir=current_dir / 'img'
    img_dir.mkdir(exist_ok=True)  #?
    for i in range(1,101):
        file_name=f"file{i}.txt"
        file_path=img_dir / file_name
        with open(file_path,'w') as file:
            file.write(f'This is file {i}')
    

