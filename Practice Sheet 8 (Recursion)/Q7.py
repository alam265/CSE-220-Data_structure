def pairStar(st):
    if len(st) == 1:
        return st
    elif st[0] == st[1]:
        return st[0]+ '*' + pairStar(st[1:])
    else:
        return st[0] + pairStar(st[1:])
    
print(pairStar('hello'))