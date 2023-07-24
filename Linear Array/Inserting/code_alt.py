def Insert(arr,idx,size):
    if idx > size or idx < 0 :
        return "Invalid Index"
    else:
        i = size 
        j = size - 1
        while j >= idx:
            arr[i] = arr[j]
            i-=1
            j-=1
        arr[idx] = 100 
        return arr 

print(Insert([1,2,3,4,5,0],4,5))