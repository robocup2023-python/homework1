def calculate(*works):
    count=0
    lists_of_index=[]
    for ele in works:
        count+=ele
    count=count/len(works)
    for i in range(len(works)):
        if works[i]>count:
            lists_of_index.append(i)
    tuples=(count,tuple(lists_of_index))

    return  tuples

