def binary_search_first_index_and_count(arr, low, high, key):
    
    while low <= high:
        mid = (low +high) // 2

        if arr[mid] == key:
          
            # Check if this is the first occurrence of the key
            if mid == low or arr[mid - 1] < key:
                count = count_occurrences(arr,mid,key)
                
                return mid,count
            else:
                high = mid-1 
                
        elif arr[mid] > key:
            high = mid-1
        else:
            low = mid+1 

   
    return 'Nothing found'  # Return the negative index and count 0 if key is not found

def count_occurrences(arr, index, key):
    count = 1
    left = index - 1
    while left >= 0 and arr[left] == key:
        count += 1
        left -= 1
    right = index + 1
    while right < len(arr) and arr[right] == key:
        count += 1
        right += 1
    return count


arr = [2,2,3,3,5,8,9,12,14,17]
idx,count = binary_search_first_index_and_count(arr,0,len(arr)-1,3)
print(idx)
print(count)