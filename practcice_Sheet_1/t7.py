arr = [3,0,0,2,0,4]

flag = False 
for i in range(len(arr)):
    if arr[i] == 0:
        flag = True 
        break 

if flag == True:
    low = 0

    if arr[0] < arr[len(arr)-1]:
        low = arr[0]
    else:
        low = arr[len(arr)-1]

    sum=0
    for i in range(len(arr)-1):
        if arr[i] == 0 :
            sum+=low
        else:
            sum=sum+(low-arr[i])


    print(sum)

else:
    print('Water can not be trapped')



