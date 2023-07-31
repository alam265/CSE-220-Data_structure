def parenBit(st):
    op = ''
    i = 0
    while i < len(st):
        if st[i] == '(':
            while st[i]!=')':
                op+=st[i]
                i+=1 
            op+=')'
        else:
            i+=1 
    return op 


print(parenBit("x(hello)"))