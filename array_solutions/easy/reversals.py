from typing import List


# Different ways to reverse String and numbers:

# def reverse_numbers(n: List[int]) -> List[int]:
#     length = len(n)
#     for i in range(length // 2):
#         # Swap elements using temp variable
#         temp = n[i]
#         n[i] = n[length - 1 - i]
#         n[length - 1 - i] = temp
#
#         # Swap elements in one line
#         # n[i], n[length - 1 - i] = n[length - 1 - i], n[i]
#     return n

# nums = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_numbers(nums)) # [7, 6, 5, 4, 3, 2, 1]

############################################################################

# def reverse_string(s: str) -> str:
#     lst = list(s)
#     length = len(lst)
#     for i in range(length // 2):
#         # Swap elements using temp variable
#         # temp = lst[i]
#         # lst[i] = lst[length - i - 1]
#         # lst[length - i - 1] = temp
#
#         # Swap elements in one line
#         lst[i], lst[length - i - 1] = lst[length - 1 - i], lst[i]
#     return "".join(lst)
#
# string = "hello"
# print(reverse_string(string)) # olleh


############################################################################

# def reverse_string(s: str) -> str:
#     s = list(s)
#     left, right = 0, len(s) - 1
#     while left < right:
#         # Swapping using helper function
#         swap(s, left, right)
#         left += 1
#         right -= 1
#     return "".join(s)
#
# # Create the above swap function:
# def swap(s, left, right):
#     temp = s[left]
#     s[left] = s[right]
#     s[right] = temp
#
# string = "hello"
# print(reverse_string(string)) # olleh


############################################################################

# def reverse_numbers(n: List[int]) -> List[int]:
#     left, right = 0, len(n) - 1
#     while left < right:
#         # Swapping using helper function
#         swap(n, left, right)
#         left += 1
#         right -= 1
#     return n
#
# # Create the above swap function:
# def swap(n, left, right):
#     temp = n[left]
#     n[left] = n[right]
#     n[right] = temp
#
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_numbers(nums))  # [7, 6, 5, 4, 3, 2, 1]

############################################################################
# Reverse words of string: Leetcode: 557. Reverse Words in a String III
# I have being asked this question by ESRI
'''
def reverse_string_words(s: str) -> str:
    st = s.split()
    for i in range(len(st)):
        st[i] = swap(st[i])
    return " ".join(st)


def swap(word):
    # word = [w[i] for i in range(len(w))]
    # Short version
    w = list(word)
    l, r = 0, len(w) - 1
    while l < r:
        w[l], w[r] = w[r], w[l]
        l += 1
        r -= 1
    return "".join(w)


print(reverse_string_words("Welcome to this ESRI!"))
# Output: emocleW ot siht !IRSE"

'''


############################################################################
# def reverse_string(s: str) -> str:
#     res = ""
#     for ch in s:
#         res = ch + res
#     return res
#
# string = "hello"
# print(reverse_string(string)) # olleh

############################################################################
# def reverse_string(s: str) -> str:
#     res = []
#     for word in range(len(s) - 1, -1, -1):
#         res.append(s[word])
#     return "".join(res)
#
# string = "hello"
# print(reverse_string(string)) # olleh

############################################################################

# def reverse_numbers(n: List[int]) -> List[int]:
#     res = []
#     for word in range(len(n) - 1, -1, -1):
#         res.append(n[word])
#     return res
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_numbers(nums))  # [7, 6, 5, 4, 3, 2, 1]

############################################################################

# def reverse_numbers(n: List[int]) -> List[int]:
#     n = n[::-1]
#     return n
#
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(reverse_numbers(nums))  # [7, 6, 5, 4, 3, 2, 1]

############################################################################

def reverse_string(s: str) -> str:
    return s[::-1]


string = "hello"
print(reverse_string(string))  # olleh
