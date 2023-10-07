def get_odders(lists):
    renewed_lists=[]
    for i in range(len(lists)):
        if i%2==0:
            renewed_lists.append(lists[i])
    return renewed_lists
