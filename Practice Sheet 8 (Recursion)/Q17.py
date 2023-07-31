def parenBit(st):
    if st[0] == '(':
        if st[-1] == ')':
            return st 
        else:
            return parenBit(st[:-1])
    else:
        return parenBit(st[1:])
    

print(parenBit("xyz(abc)123"))