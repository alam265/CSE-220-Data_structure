def count(n):
    rem = n%10
    if  n == 0:
        return 0
    elif rem == 7:
        return 1 + count(n//10)
    else:
        return count(n//10)

print(count(717))