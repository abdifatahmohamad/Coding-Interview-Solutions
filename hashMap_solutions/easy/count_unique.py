# Given two strings, create a function that returns the total number of unique characters from the combined string.
'''
Test Cases:
count_unique("apple", "play") ➞ 5
"appleplay" has 5 unique characters:
"a", "e", "l", "p", "y"

count_unique("sore", "zebra") ➞ 7

count_unique("a", "soup") ➞ 5
'''

# Solution using HashMap O(N) Time & Space


def count_unique(s1, s2):
    d = {}
    total = 0
    for k, v in enumerate(s1):
        d[v] = d.get(v, 0) + 1
        if k > 1:
            total += 1

    for k, v in enumerate(s2):
        d[v] = d.get(v, 0) + 1
        if k > 1:
            total += 1

    return total


print(count_unique("apple", "play"))
# Output: 5
