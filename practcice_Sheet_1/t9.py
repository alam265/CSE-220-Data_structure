import numpy as np

arr = np.array([3,1,3,3,2])

for i in range(len(arr)):
    c=1
    if arr[i]!=-1:
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                c +=1
                arr[j] = -1
        
        if c > len(arr)/2:
            print(arr[i])
            break
        print(-1)
       
