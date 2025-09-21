def ReverseArr(arr):
    i=0
    j = len(arr)-1
    while(i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    return arr

print(ReverseArr([1,3,5,7,9,11,13,2,4,0,100]))