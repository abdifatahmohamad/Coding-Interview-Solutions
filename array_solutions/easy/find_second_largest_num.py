from typing import List


def second_largest(nums: List[int]) -> int:
    # Solution 1:
    largest = None
    sec_largest = None
    for curr_num in nums:
        if largest == None:
            largest = curr_num
        elif curr_num > largest:
            sec_largest = largest
            largest = curr_num

        elif sec_largest == None:
            sec_largest = curr_num
        elif curr_num > sec_largest:
            sec_largest = curr_num
    return sec_largest

    # Solution 2: by removing largest num using max built-in func
    nums.remove(max(nums))
    return max(nums)


nums = [1, 3, 4, 5, 0, 2]
# Output: 4
print(second_largest(nums))
