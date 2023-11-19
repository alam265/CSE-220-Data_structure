def binary_search_first_index_and_count(arr, low, high, key):
    global count
    while low <= high:
        mid = (low +high) // 2

        if arr[mid] == key:
            count+=1
            # Check if this is the first occurrence of the key
            if mid == low or arr[mid - 1] < key:
               
                return mid
            else:
                high = mid-1 
                
        elif arr[mid] > key:
            high = mid-1
        else:
            low = mid+1 

    return 'Nothing found'  # Return the negative index and count 0 if key is not found

count = 0
arr = [2,2,3,3,5,8,9,12,14,17]
x = binary_search_first_index_and_count(arr,0,len(arr)-1,17)
print(x)
print(count)