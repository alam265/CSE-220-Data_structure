def strCount(st,subst):
    if st == '':
        return 0
    elif st[:len(subst)] == subst:
        return 1 + strCount(st[len(subst):],subst)
    else:
        return strCount(st[1:],subst)
    

print(strCount("catcowcat","cow"))