def BinSearch(arr,left,right,key):
    if left > right :
        return False 
    else:
        mid = (left+right)//2 
        if arr[mid]==key:
            return mid 
        elif key > arr[mid]:
            return BinSearch(arr,mid+1,right,key)
        else:
            return BinSearch(arr,left,mid-1,key)

arr = [1,2,3,4,5,6,7]        
print(BinSearch(arr,0,len(arr)-1,5))