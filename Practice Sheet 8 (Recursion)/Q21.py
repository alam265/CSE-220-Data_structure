def allStar(st):
    if len(st) == 1:
        return st[0]
    else:
        return st[0]+'*' + allStar(st[1:])
    

print(allStar("abc"))