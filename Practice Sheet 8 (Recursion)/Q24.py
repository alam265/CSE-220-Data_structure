def nestParen(st):
    if len(st) == 0:
        return True 
    elif st[0] == '(' and st[-1] != ')':
        return False 
    elif st[0] == '(' and st[-1]==')':
        return nestParen(st[1:-1])
    return nestParen(st[1:])


print(nestParen("((x)"))