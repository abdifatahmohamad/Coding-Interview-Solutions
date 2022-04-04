# Create a function that takes a string and returns the letters that occur only once.
from collections import OrderedDict


# Solution1
def find_letters(word):
    d = OrderedDict()
    for char in word:
        d[char] = d.get(char, 0) + 1

    res = []
    for ch in d:
        if d[ch] > 1:
            continue
        else:
            res.append(ch)
    return res


# Solution2
def find_letters(word):
    bucket = [0] * 26
    for char in word:
        bucket[ord(char) - ord("a")] += 1

    res = []
    for ch in word:
        if bucket[ord(ch) - ord("a")] > 1:
            continue
        else:
            res.append(ch)
    return res


print(find_letters("monopoly"))  # ["m", "n", "p", "l", "y"]

print(find_letters("balloon"))  # ["b", "a", "n"]

print(find_letters("analysis"))  # ["n", "l", "y", "i"]
