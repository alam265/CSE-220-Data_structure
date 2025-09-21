def InsertionSort(arr,left,right):
    if left >= right:
        return 
    else:
        InsertionSort(arr,left,right-1)
        key = arr[right]
        j = right - 1 
        while j >-1 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1 
        arr[j+1] = key 


arr = [2,5,1,0,-7,3,-6]

InsertionSort(arr,0,len(arr)-1)

print(arr)