# Given two strings, create a function that returns the total number of unique characters from the combined string.
'''
Test Cases:
count_unique("apple", "play") ➞ 5
"appleplay" has 5 unique characters:
"a", "e", "l", "p", "y"

count_unique("sore", "zebra") ➞ 7

count_unique("a", "soup") ➞ 5
'''

# Solution O(N) Time & Space


def count_unique(s1, s2):
    res = []
    for ch1 in s1:
        res.append(ch1)

    for ch2 in s2:
        res.append(ch2)

    return len(set(res))

# Easy Solution


def count_unique(s1, s2):
    unique = []
    for char in (s1 + s2):
        if char not in unique:
            unique.append(char)

    return len(unique)


print(count_unique("apple", "play"))
# Output: 5
