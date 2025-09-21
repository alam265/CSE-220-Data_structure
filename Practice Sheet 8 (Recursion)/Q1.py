def SumOfDigit(num):
    if num <10: 
        return num 
    else:
        res = num//10
        rem = num%10 
        return rem + SumOfDigit(res)
    
print(SumOfDigit(526))