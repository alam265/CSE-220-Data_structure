def count11(st):
    if len(st)==0:
        return 0
    elif st[:2] == '11':
        return 1 + count11(st[2:])
    else:
        return count11(st[1:])
    

print(count11("abc11x11x11"))