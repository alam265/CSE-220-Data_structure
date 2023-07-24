import numpy as np 

def dlt(arr,idx,length):
    i = idx 
    j = idx +1 
    while j < length   :
        arr[i] = arr[j]
        i+=1
        j+=1
    
         
    arr[length-1] = 0 
    return arr 


print(dlt(np.array([1,3,5,7,9]),1,5))