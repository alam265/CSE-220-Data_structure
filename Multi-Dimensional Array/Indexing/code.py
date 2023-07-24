import numpy as np

O_dimension = [4,4,8]
D_dimension = [3,1,7]

value = 10

arr = np.zeros(128,dtype=int)


sum = 0

for i in range(len(D_dimension)):
    multi=1
    for j in range(i+1,len(O_dimension)):
        multi*=O_dimension[j]
    sum += multi * D_dimension[i]
arr[sum] = value 

print(sum)
print(arr)
