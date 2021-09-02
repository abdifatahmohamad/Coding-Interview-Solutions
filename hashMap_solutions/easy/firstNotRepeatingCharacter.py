def firstNotRepeatingCharacter(s):
    mapping = {}
    for char in s:
        mapping[char] = mapping.get(char, 0) + 1

    for i in range(len(s)):
        if mapping[s[i]] == 1:
            return i

    return -1


print(firstNotRepeatingCharacter("aaabcccdeeef"))  # Index 3
print(firstNotRepeatingCharacter("aabbcc"))  # -1
