def create_files():
    import pathlib
    dir=pathlib.Path.cwd()
    img_dir_name=dir / "img"
    img_dir_name.mkdir(exist_ok=True)
    for i in range(100):
        with open(img_dir_name / f'{i}.txt','w') as  f:
            pass
create_files()