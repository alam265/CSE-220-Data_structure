def strDist(str, sub):
    # Find the first occurrence of sub in str
    start = -1
    for i in range(len(str) - len(sub) + 1):
        if str[i:i + len(sub)] == sub:
            start = i
            break

    # Find the last occurrence of sub in str
    end = -1
    for i in range(len(str) - 1, -1, -1):
        if str[i:i + len(sub)] == sub:
            end = i
            break

    # Calculate the length of the substring between start and end
    length = end - start + len(sub)

    return length

# Test cases
print(strDist("catcowcat", "cat"))      # Output: 9
print(strDist("catcowcat", "cow"))      # Output: 3
print(strDist("cccatcowcatxx", "cat"))  # Output: 9


