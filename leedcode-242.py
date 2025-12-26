def anagram(s,t):
    if len(s)==len(t):
        s1=sorted(s)
        t1=sorted(t)
        if (s1==t1):
            return True
        else:
            return False
    else:
        return False