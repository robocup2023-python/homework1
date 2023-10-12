from pathlib import Path 
file_dir='./test/'
test_dir =Path(file_dir)
for path in test_dir.iterdir():
    path_name=path.name
    if "python" in path_name:
        path_name=path_name.replace('python',"class")
    path1=path.rename(file_dir+path_name)
    with open(path1,'r') as f:
        content=f.read()
        if "python" in content:
            content=content.replace("python",'class')
    with open(path1,'w') as f:
        f.write(content)

