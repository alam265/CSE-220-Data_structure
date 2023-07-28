def maximum(a,b):
    return a if a>=b else b 

def findmax(arr,left,right):
    if left == right:
        return arr[left]
    else:
        mid = (left+right)//2
        left_side_max = findmax(arr,left,mid)
        right_side_max = findmax(arr,mid+1,right)
        return maximum(left_side_max,right_side_max)
    


arr = [1,20,3,49,6,7]

print(findmax(arr,0,len(arr)-1))