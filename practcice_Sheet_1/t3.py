import numpy as np

arr = np.array([1,2,3,7,5])

def pos(arr):
    for i in range(len(arr)):
        sum=0

        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum == 12:
                return (i+1,j+1)
   
print(pos(arr))    