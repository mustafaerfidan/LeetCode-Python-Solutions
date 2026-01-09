def firstUniqChar(s):
    sözlük={}
    for i in s:
        if i in sözlük:
            sözlük[i]=sözlük[i]+1
        else:
            sözlük[i]=1
    
    for i,harf in enumerate(s):

        if sözlük[harf]==1:
            return i
    return -1 
        

    



    