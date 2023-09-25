def anagram(s:str ,t:str):
    
    
    arr = []
    for i in s:
        arr.append(i)
    for j in t:
        if j in arr:
            arr.remove(j)
    if len(arr) == 0:
        print('true')
    else:
        print('false')

anagram('anagram', 'nagaram')

#this is correct