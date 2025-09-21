def countABC(st):
    if st == '':
        return 0 
    elif st[:3] == 'abc' or st[:3] == 'aba':
        return 1+ countABC(st[3:])
    else:
        return countABC(st[1:])
    

print(countABC('abcxxabcxxaba'))