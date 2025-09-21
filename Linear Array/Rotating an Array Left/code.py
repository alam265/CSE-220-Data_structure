def RL(arr):
    temp = arr[0]
    for i in range(0,len(arr)-1):
        arr[i]=arr[i+1]
    arr[i+1] = temp
    return arr


print(RL([1,2,3,4,5]))