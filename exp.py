def changePi(string):
    output = ""

    
    i = 0
    while i < len(string):
        
        if i + 1 < len(string) and string[i:i + 2] == "pi":
            output += "3.14"
            i += 2
        else:
            output += string[i]
            i += 1

    return output

print(changePi('xpix'))