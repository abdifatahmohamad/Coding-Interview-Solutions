def firstNotRepeatingCharacter(s):
    mapping = {}
    for char in s:
        mapping[char] = mapping.get(char, 0) + 1

    for i, el in enumerate(s):
        if mapping[s[i]] == 1:
            return i

    return -1


print(firstNotRepeatingCharacter("aaabcccdeeef"))
print(firstNotRepeatingCharacter("aabbcc"))
