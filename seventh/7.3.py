def modification():
    with open('test.txt','r+') as f1:
        content=f1.read()
        last=f1.tell()
        print(last)
        f1.seek(0,0)
        f1.write('python\r\n'+content)
        f1.seek(last+3,0)
        f1.write('python')
modification()