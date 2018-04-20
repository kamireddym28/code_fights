def firstNotRepeatingCharacter(s):
    dict1 = {}
    
    for i in s:
        if i in dict1:
            dict1[i] += 1    
        else:
            dict1[i] = 1
        
    for i in s:
        if dict1[i] == 1:
            return i
    return '_'
    
