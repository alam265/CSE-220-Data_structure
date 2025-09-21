arr =[7,85,54,16,11,30]
#arr=[20,13,33,12]
i=0
while i<len(arr):
    j = i +1
    while j<len(arr):
        if arr[i]<arr[j]:
            print(arr[j],'is greater than ', arr[i])
            break
        else:
            j+=1
        if j==len(arr):
            print(f'No next elem grtr than ',arr[i])
    
    i+=1
print(f"No next elem grtr than ",arr[len(arr)-1])