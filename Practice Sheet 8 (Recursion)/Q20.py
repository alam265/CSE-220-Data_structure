def find6(arr,idx):
    if idx ==len(arr) :
        return False 
    elif arr[idx] == 6:
        return True
    return find6(arr,idx+1)


print(find6([1, 9, 4], 0))