# Using hash map O(N) Time and Space
def first_non_rep(s: str) -> str:
    mapping = {}
    for char in s:
        mapping[char] = mapping.get(char, 0) + 1

    for i in range(len(s)):
        char = s[i]
        if mapping[char] == 1:
            return char
    return None


# Using bucket and fixed array size:
# O(N) Time || O(1) Space
def first_non_rep(s: str) -> str:
    if not s:
        return "String is empty!"

    if len(s) == 1:
        return s

    # English alphabet lower case is 26
    bucket = [0] * 26
    for ch in s:
        # Increment each alphapet location
        index = ord(ch) - ord("a")
        bucket[index] += 1

    for ch in s:
        index = ord(ch) - ord("a")
        # Check for the alphabet with count 1
        if bucket[index] == 1:
            return ch
    return "Not found."


# Using two pointers:
def first_non_rep(s: str) -> str:
    if not s:
        return "String is empty!"

    if len(s) == 1:
        return s

    p1, p2 = 0, 1
    while p2 < len(s):
        if s[p1] != s[p2]:
            return s[p1]
        p1 += 2
        p2 = p1 + 1

        if len(s) % 2 == 1 and p2 + 1 == len(s) - 1:
            return s[-1]
        elif len(s) % 2 == 1 and p2 == len(s) and s[p2-1] != s[p1-1]:
            return s[-1]
    return "Not fount!"


# Test Cases:
s1 = "aabccd"  # -> d
s2 = "aabbcf"  # -> c
s3 = "kllm"  # -> k
s4 = "a"  # -> a

print(first_non_rep(s4))
