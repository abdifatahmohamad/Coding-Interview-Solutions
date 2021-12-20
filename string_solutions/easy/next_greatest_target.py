# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

def next_greatest_letter(letters, target) -> str:
    for c in letters:
        if ord(c) > ord(target):
            return letters[c]
    return letters[0]


# letters = ['a', 'b']
# target = 'z'
# # Output: a


# letters = ['c', 'f', 'j']
# target = 'a'
# # Output: c

# letters = ['c', 'f', 'j']
# target = 'c'
# # Output: f

letters = ['c', 'f', 'j']
target = 'j'
# Output: c

# letters = ['c', 'f', 'j']
# target = 'd'
# # Output: f


print(next_greatest_letter(letters, target))
