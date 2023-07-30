def changePi(st):
    if st =='':
        return ""
    elif st[:2] == 'pi':
        return '3.14' + changePi(st[2:])
    else:
        return st[0] + changePi(st[1:])
    
print(changePi('xpix'))