def Fibonacci(nth):
    if nth == 1 or nth == 0:
        return nth 
    return Fibonacci(nth-1)+Fibonacci(nth-2)



print(Fibonacci(6))