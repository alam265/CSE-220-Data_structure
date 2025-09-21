def bunnyEars(n):
    if n == 0:
        return 0 
    else:
        return 2 + bunnyEars(n-1)
    

print(bunnyEars(0))