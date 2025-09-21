def Insertion(arr,size,elm,idx):
    if size == len(arr):
        print('No space left, cam not insert')
        return 
    if idx > len(arr) or idx <0 :
        print("invalid Index")
        return
    else:
        for i in range(size,idx-1,-1):
            arr[i] = arr[i-1]
        arr[idx] = elm 

    return arr


print(Insertion([1,2,3,4,5,None,None],5,100,13))
