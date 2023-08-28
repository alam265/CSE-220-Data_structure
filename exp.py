
def BinaryToDecimal(st):
    def BinTodec(st,i=0,dec=0):
        if i==len(st):
            return dec 
        if st[i] == '0':
            dec=2*dec
        else:
            dec=2*dec+1
        return BinTodec(st,i+1,dec)
    x = BinTodec(st)
    return x 

print(BinaryToDecimal("1101"))
