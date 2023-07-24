lst = [7,85,54,16,11,30]

for i in range(len(lst)):
    flag = False
    for j in range(i+1,len(lst)):
        if lst[j] > lst[i]:
            print(f"{lst[j]} is greater than {lst[i]}")
            flag = True 
            break
        else:
            flag = False 
    if flag == False:
        print(f"No next elem is grtr thn {lst[i]}")

        