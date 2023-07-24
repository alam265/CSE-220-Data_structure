def deleteElement(arr,idx,size):
    for i in range(idx+1,size+1):
        arr[i-1]=arr[i]
    arr[size-1]=None 
    return arr 

print(deleteElement([10,6,8,11,12,20,None],2,6))
