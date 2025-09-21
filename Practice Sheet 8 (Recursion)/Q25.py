def stDist(st,sub):
    if len(st) < len(sub):
        return 0 
    if st[:len(sub)] == sub:
        if st[-len(sub):] == sub:
            return len(st)
        return stDist(st[:-1],sub)
    else:
        return stDist(st[1:],sub)


print(stDist("cccatcowcatx",'cat'))