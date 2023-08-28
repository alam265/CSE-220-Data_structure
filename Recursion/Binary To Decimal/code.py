def BinToDec(st,idx,sum=0,p=0):
    if idx == -1:
        return sum 
    sum = sum + int(st[idx]) *pow(2,p)
    return BinToDec(st,idx-1,sum,p+1)
    

print(BinToDec("1101",3))    # 3 is lenght-1 of st