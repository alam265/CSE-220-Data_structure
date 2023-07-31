def countPairs(st):
    if len(st) <=2:
        return 0 
    elif st[0] == st[2]:
        return 1 + countPairs(st[1:])
    return countPairs(st[1:])


print(countPairs('xaxa'))