# How will you check whether one string is a permutation of another string?

from collections import Counter

'''
# Using hash map
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    mapping = Counter(str1)
    for ch in str2:
        if ch in mapping:
            mapping[ch] -= 1
        else:
            return False

        if mapping.get(ch) < 0:
            return False
    return True

'''

# Using bucket


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    bucket = [0 for _ in range(128)]  # Assuming ASCII character set
    for ch in str1:
        bucket[ord(ch)] += 1

    for ch in str2:
        bucket[ord(ch)] -= 1
        if bucket[ord(ch)] < 0:
            return False
    return True


print(is_permutation("abcd", "dcba"))  # True
print(is_permutation("abcd", "dcbx"))  # False
