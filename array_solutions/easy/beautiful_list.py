def listBeautifier(nums):
    if len(nums) == 0:
        return nums

    left, right = 0, len(nums) - 1
    while nums[left] != nums[right] and left < right:
        left += 1
        right -= 1
    nums = nums[left:right + 1]
    return nums


# List has be to an odd:
# nums = [3, 4, 2, 4, 38, 4, 5, 2, 15]
# nums = [1, 4, -5]
# nums = []
# nums = [10, 2, 10, 9, 7, 3, 8, 5, 3, 2, 8, 7]
# nums = [8, 5, 1, 2, 3, 8, 1, 10, 5, 1, 4, 6, 9, 2, 8, 8, 9, 4, 10, 3]
nums = [10, 8, 10]
print(listBeautifier(nums))


# https://app.codesignal.com/arcade/python-arcade/meet-python/ZiezPAoWeaK9ThXvQ
