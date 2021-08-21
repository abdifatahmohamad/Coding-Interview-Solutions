from typing import List


# Solution 2: Using hash map
def remove_duplicates(nums: List[int]) -> List[int]:
    mapping = {}
    for num in nums:
        mapping[num] = mapping.get(num, 0) + 1

    for i in range(len(nums)):
        el = nums[i]
        if mapping[el] > 1:
            mapping[el] -= 1
    return list(mapping.keys())


nums = [1, 2, 2, 3, 3, 3, 3]
print(remove_duplicates(nums))  # [1, 2, 3]
