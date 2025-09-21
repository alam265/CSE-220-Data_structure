import numpy as np

arr1 = np.array([6,2])
arr2 = np.array([85, 25, 1, 32, 54, 6])


new_arr = np.zeros(len(arr1)+len(arr2),dtype=int)


for i in range(len(arr1)):
    new_arr[i] = arr1[i] 


k = len(arr1)
for i in range(len(arr2)):
    flag = False
    for j in range(len(arr1)):
        if arr2[i]==arr1[j]:
            flag = True 
            
            break
    if flag== False:
        new_arr[k] = arr2[i]
        k += 1

print(new_arr)

