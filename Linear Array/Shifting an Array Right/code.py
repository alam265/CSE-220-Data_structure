def RightShift(arr):
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0]= None
    return arr 

print(RightShift([1,2,3,4,5]))