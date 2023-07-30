def arr11(arr,left):
    if left == len(arr):
        return 0
    elif arr[left] == 11:
        return 1 + arr11(arr,left+1)
    else:
        return arr11(arr,left+1)
    
arr = [1,2,11,6,11]
print(arr11(arr,0))