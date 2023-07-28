def SLlength(st):
    if st == "":
        return 0 
    return 1 + SLlength(st[1:])


print(SLlength("abc"))