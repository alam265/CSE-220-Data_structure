def insert(arr,n):
    i = n 
    temp = arr[n]

    while i >1 and temp > arr[i//2]:
        arr[i] = arr[i//2]
        i = i//2 
    arr[i] = temp

def create_heap(arr):
    for i in range(2,len(arr)):
        insert(arr,i)
    return arr
print(create_heap([None,10,20,30,25,5,40,35]))

