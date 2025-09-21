def array220(arr,left):
    if left == len(arr)-1:
        return False 
    elif arr[left]*10 == arr[left+1]:
        return True
    return array220(arr,left+1)


arr = [3]
print(array220(arr,0))