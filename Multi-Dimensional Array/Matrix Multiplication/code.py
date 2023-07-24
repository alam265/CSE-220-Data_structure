import numpy as np 

arr1 = np.array([[1,5],[56,11],[9,10]])
arr2 = np.array([[1,9,12],[4,8,10]])

result  = np.zeros((3,3),dtype=int)


for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        sum=0
        for k in range(len(arr1[0])):
            sum += arr1[i][k]*arr2[k][j]
            
        result[i][j] = sum 
        
        


print(result)
