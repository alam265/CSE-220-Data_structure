def exp(a ,n):
    if n==0:
        return 1 
    elif n%2 == 0:
        temp = exp(a,n/2)
        return temp*temp
    else:
        temp = exp(a,(n-1)/2)
        return temp*temp*a 
    
print(exp(2,6))                             