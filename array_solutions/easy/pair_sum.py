from typing import List


def pair_sum(array1: List[int], array2: List[int], target: int) -> List[int]:

    for i in range(len(array2)):
        if array2[i] + array1[i] == target:
            return [array2[i], array1[i]]

    return "No pairs found that adds up to the target!"


nums1 = [-1, 3, 8, 2, 9, 5]
nums2 = [4, 1, 2, 10, 5, 20]
target = 22
print(pair_sum(nums1, nums2, target))
