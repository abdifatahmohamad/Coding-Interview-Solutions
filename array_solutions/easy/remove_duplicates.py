from typing import List


# SOLUTION 1: using built-in set
# def remove_duplicates(nums: List[int]) -> List[int]:
#     return list(set(nums))

# O(N) Time and Space
def remove_duplicates(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res


############################
def remove_duplicates(nums: List[int]) -> List[int]:
    mapping = {}
    res = []
    for num in nums:
        if num not in mapping:
            res.append(num)
            mapping[num] = 1
    return res


nums = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3]
print(remove_duplicates(nums))  # [1, 2, 3]
