def countHi(st):
    if st == '':
        return 0 
    elif st[0] != 'x' and st[1:3] == 'hi':
        return 1+ countHi(st[3:])
    else:
        return  countHi(st[1:])
    

print(countHi("ahibhi"))