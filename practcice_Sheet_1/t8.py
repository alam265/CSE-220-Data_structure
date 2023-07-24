import numpy as np 

arr = np.array([1,2,3,4,5])

i=0
j =i+1

while j < len(arr) :
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 
    i+=2
    j+=2 



print(arr)
 