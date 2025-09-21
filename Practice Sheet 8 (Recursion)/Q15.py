def endX(st):
    if len(st)==0:
        return '' 
    elif st[0]=='x':
        return endX(st[1:])+st[0]
    else:
        return st[0]+endX(st[1:])


print(endX("xxhixx"))