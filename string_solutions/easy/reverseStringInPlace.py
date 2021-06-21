# Write a function that reverses the string in place.
# O(N) Time | O(1)Space
# SOLUTION - Using two pointers
def reverseStringInPlace(s):
    left = 0
    right = len(s) - 1
    while left < right:
        # Swap characters:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


print(reverseStringInPlace('hello'))
print(reverseStringInPlace('car'))
print(reverseStringInPlace('house'))
