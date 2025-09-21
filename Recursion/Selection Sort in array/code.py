def findMinIdx(arr,left):
    if left == len(arr)-1:
        return left
    else:
        minRest = findMinIdx(arr,left+1)
        minIdx = left
        if arr[minRest] < arr[left]:
            minIdx = minRest 
        return minIdx 
    
def swap(a,b):
    arr[a] , arr[b] = arr[b] , arr[a] 

def SelectionSort(arr,left):
    if left == len(arr) -1:
        return 
    else:
        minidx = findMinIdx(arr,left)
        swap(left,minidx)
        SelectionSort(arr,left+1)


arr = [4,1,7,0,3,6,98,12,5,-45,-3]

SelectionSort(arr,0)

print(arr)



    