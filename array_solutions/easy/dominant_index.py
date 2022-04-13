def dominantIndex(nums):
    if len(nums) == 1:
        return 0

    largest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]

    # finding max index of the array nums
    max_index = nums.index(largest)
    for i in range(len(nums)):
        if nums[i] != largest and largest < 2 * nums[i]:
            return -1

    return max_index


print(dominantIndex([3, 6, 1, 0]))  # 1
print(dominantIndex([1, 2, 3, 4]))  # -1
# print(dominantIndex([1])) # 0
