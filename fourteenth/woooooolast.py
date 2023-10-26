from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from pathlib import Path

def deal_with_a_file(file):
    pool_t = ThreadPoolExecutor(4)
    l = {}
    for i in range(4):
        res = pool_t.submit(deals, file[i])
        l[i] = pd.Series(res.result())
    df = pd.concat([l[0], l[1], l[2], l[3]], axis=1, join='outer', keys=[1, 2, 3, 4])
    df["sum"] = df.sum(axis=1)

    df = df['sum']
   
    return df
import xml.etree.ElementTree as ET
def deals(file):
    tree=ET.parse(file)
    root=tree.getroot()
    text=""
    for elem in root.iter():
        if elem.text:
            text+=(" "+elem.text+"")
    lt=text.split()
    dic = {}
    for i in lt:
        if not (i in dic):
            dic[i] = 1
        else:
            dic[i] += 1 
    
    A = pd.Series(dic)
    return A 

if __name__ == "__main__":
    pool_p = ProcessPoolExecutor(4)
    location = Path.cwd()
    location = location / "download"
    glob_files = location.glob("**/*.xml")
    ls = []
    #data=pd.Dataframe()
    flag = False
    for idx, element in enumerate(glob_files):
        ls.append(element)
        if len(ls) % 4 == 0:
            res = pool_p.submit(deal_with_a_file, ls)
            ls = []
            if not flag:
                data=res.result()
                #data = pd.concat([data, res.result()], axis=1, ignore_index=False)
                flag = True
            else:
                data = pd.concat([data, res.result()], axis=1, ignore_index=False)
    data["sum_all"] = data.sum(axis=1)
    data=data["sum_all"]
    data.to_csv("./outcome.csv")
