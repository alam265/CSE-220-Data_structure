def countX(st):
    if st =='':
        return 0 
    elif st[0] == 'x':
        return 1 + countX(st[1:])

    return countX(st[1:])


print(countX('xxhixx'))