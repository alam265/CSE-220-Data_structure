def noX(st):
    if len(st)==0:
        return ""
    elif st[0]=='x':
        return ''+ noX(st[1:])
    else:
        return st[0]+ noX(st[1:])
    

print(noX('acx'))