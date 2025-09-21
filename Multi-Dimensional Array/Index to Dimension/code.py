import numpy as np 

idx = 120

d=[4,4,8]

lst=[]
for i in range(1,len(d)):
    multi=1
    for j in range(i,len(d)):
        multi*=d[j]
    res = idx//multi 
    rem = idx % multi
    lst.append(res)
    idx = rem 
    
lst.append(rem)


print(lst)