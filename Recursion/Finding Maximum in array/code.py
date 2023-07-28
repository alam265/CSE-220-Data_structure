def maximum(a,b):
    return a if a>=b else b 

def findMax(arr,left):
    if left == len(arr)-1:
        return arr[left]
    else:
        maxRest = findMax(arr,left+1)
        return maximum(arr[left],maxRest)
    


arr = [10,20,50,23,76,23,56]

print(findMax(arr,0))