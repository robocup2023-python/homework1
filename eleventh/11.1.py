import os

import threading
def rename_file(file_path ,new_name):
    os.rename(file_path,new_name)
def thread_function(file_path,new_name):
    rename_file(file_path,new_name)
    threads=[]
    for i in range(5):
        t=threading.Thread(target=thread_function,args=(file_path,new_name))
        threads.append(t) 
        t.start()
    for t in threads:
            t.join()
