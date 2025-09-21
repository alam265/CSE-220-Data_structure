import numpy as np 

arr = np.array([1, -1, 3, 2, -7, -5, 11, 6])

new_arr = np.zeros(len(arr),dtype=int)

k = 0
for i in range(len(arr)):
    if arr[i]>0:
        new_arr[k] = arr[i]
        k+=1

for j in range(len(arr)):
    if arr[j]< 0 :
        new_arr[k] = arr[j]
        k+=1


print(new_arr)