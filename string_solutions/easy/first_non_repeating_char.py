# Using hash map O(N) Time and Space
def first_non_repeating_char(string: str) -> str:
    mapping = {}
    for char in string:
        mapping[char] = mapping.get(char, 0) + 1

    for i in range(len(string)):
        char = string[i]
        if mapping[char] == 1:
            return char
    return None


# Test Cases:
s1 = "aabccd"  # -> b
s2 = "aabbcf"  # -> c
s3 = "kllm"  # -> k
s4 = "a"  # -> a

print(first_non_repeating_char(s4))

#########################################################


# Using bucket and fixed array size:
def first_non_repeating_char(string: str) -> str:
    arr = [0] * 256
    for i in range(len(string)):
        if string[i] != " ":
            num = ord(string[i])
            arr[num] += 1

    res = ""
    for i in range(len(string)):
        if arr[ord(string[i])] == 1:
            res = string[i]
            break
    return res


s1 = "aabccd"  # -> b
print(first_non_repeating_char(s1))
