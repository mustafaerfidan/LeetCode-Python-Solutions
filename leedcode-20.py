def parantezler(s):
    stack=[]
    eslesme = { ")" : "(", "}" : "{", "]" : "[" }
    for i in s :
        if i =="(" or i=="{" or i== "[" :
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            else:
                if eslesme[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
    if len(stack)==0:
        return True
    else:
        return False

