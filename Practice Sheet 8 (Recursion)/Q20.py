def find6(arr,idx):
    if idx ==len(arr)-1 :
        return False 
    elif arr[idx] == 6:
        return True
    return find6(arr,idx+1)


print(find6([1, 6, 4], 0))