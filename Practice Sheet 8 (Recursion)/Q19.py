def changeX(st):
    if len(st)==0:
        return ''
    elif st[0] == 'x':
        return 'y' + changeX(st[1:])
    return st[0]+changeX(st[1:])


print(changeX("codex"))