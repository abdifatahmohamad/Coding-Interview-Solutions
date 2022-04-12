from collections import OrderedDict


# CodePath easy problem
def maximum_occurrence_character(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    max_occurrence = float("-inf")
    res = ""
    for char, value in frequency.items():
        if value > max_occurrence:
            max_occurrence = value
            res = char

    return res


print(maximum_occurrence_character("abbbaacc"))
