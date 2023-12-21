n = int(input("Enter nth: "))
F = [None]*(n+1)
def fib(n):
    if n ==1 or n==0:
        return n 
    elif F[n] is None:
        F[n] = fib(n-1) + fib(n-2)
    return F[n]



print(fib(n))
