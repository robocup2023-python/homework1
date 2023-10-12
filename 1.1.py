with open('condon.txt','r') as f:#codon-->diccondonamino
    f.readline()
    lists=f.read().split()
    dic_condon_amino={}
    for i in range(len(lists)):
        if i%2==0:
            codon=lists[i]
        else:
            dic_condon_amino[codon]=lists[i]
def transcript(list_of_DNA:list):
    '''translate dna to mrna'''
    flag=False
    list_of_mRNA=[]
    list_of_DNA=list_of_DNA.replace("T","U").rstrip()
    begin=list_of_DNA.find("AUG")
    if begin==-1:
        return ''
    else:
        for i in range(begin+3,len(list_of_DNA)+1,3):
            list_of_mRNA.append(dic_condon_amino[list_of_DNA[begin:i]])
            begin=i
            if list_of_mRNA[-1]=="stop":
                list_of_mRNA.pop()
                flag=not flag
                break
        if flag==False:
            raise IndexError("THE LISTS OF DNA IS WRONG!")
        else:
            return list_of_mRNA
def read_protein():
    with open("protein.txt",'r') as f1:#MLPV
        seq_lists={}
        for i in f1:
            if 'seq' in i:
                title=i
            else:
                seq_lists[title]=i#seq-->DNA
        return seq_lists
def translate(dictt:dict):
    for index_ in dictt.keys():
        string_of_DNA=dictt[index_]
        dictt[index_]=''.join(transcript(string_of_DNA))
    return dictt
def create_files(dict_of_protein):
    with open("protein.txt","w") as  f:
        for i in dict_of_protein.keys():
            f.write(f"{i}\n\t{dict_of_protein[i]}\n")
create_files(translate(read_protein()))
# BATGATCCAATCATGA


            


