def strCopies(st, sub, n):
    if n==0:
        return True 
    
    elif len(st) < len(sub):
        return False
     
    elif st[:len(sub)] == sub:
        return strCopies(st[len(sub):],sub,n-1)
    
    return strCopies(st[1:],sub,n)
  


print(strCopies("catcowcat", "cat", 2))  # Output: True
print(strCopies("catcowcat", "cow", 2))  # Output: False
print(strCopies("catcowcat", "cow", 1))  # Output: True
