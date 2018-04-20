def firstDuplicate(a):
    dict = {}
    for i in range(len(a)):
        if a[i] not in dict:
            dict[a[i]] = a[i] 
        else:
            return a[i]
    return -1
