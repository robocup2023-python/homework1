def compare_files():
    with open('test.txt') as f1:
        line1=f1.readline()
        l1=f1.tell()

    with open('copy_test.txt') as f2:
        line2=f2.readline()
        l2=f2.tell()
    count=1
    while line1 or line2:
        if line1!=line2:
            print(count,end=" ")
        count+=1
        with open('test.txt') as f1:
            f1.seek(l1,0)
            line1=f1.readline()
            l1=f1.tell()

        with open('copy_test.txt') as f2:
            f2.seek(l2,0)
            line2=f2.readline()
            l2=f2.tell()

compare_files()