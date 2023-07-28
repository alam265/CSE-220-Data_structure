import numpy as np 

arr = np.array([1,3,5,7,9])

def contains(arr,left,key):
    if left == len(arr)-1:
        return False 
    elif arr[left] == key:
        return True 
    return contains(arr,left+1,key)



print(contains(arr,0,7))