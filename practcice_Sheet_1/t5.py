import numpy as np

arr = np.array([0, 2, 1, 2, 0])


for i in range(len(arr)):
    min_loc = i 
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_loc]:
            min_loc = j 
    temp = arr[i]
    arr[i] = arr[min_loc]
    arr[min_loc] = temp

print(arr)
print(arr[3-1])

