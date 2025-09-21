def LeftShift(arr):
    for i in range(0,len(arr)-1,1):
        arr[i] = arr[i+1]
    arr[i+1] = None
    return arr 

print(LeftShift([1,2,3,4,5]))