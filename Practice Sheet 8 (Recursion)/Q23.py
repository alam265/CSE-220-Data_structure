def stringClean(s):
    if len(s) == 1:
        return s

    if s[0] == s[1]:
        return stringClean(s[1:])
    else:
        return s[0] + stringClean(s[1:])


print(stringClean("yyzzza"))  
print(stringClean("abbbcdd"))
print(stringClean("Hello"))    
