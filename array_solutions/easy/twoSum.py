# O(N^2) Time, O(1) Space
def twoNumberSum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


# O(N log N) Time, O(1) Space
def twoNumberSum(nums, target):
    nums.sort()  # Array is sorted under the hood here
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


# O(n) time | O(n) space
def twoNumberSum(array, target):
    mapping = {}
    for num in array:
        potentialMatch = target - num
        if potentialMatch in mapping:
            return [potentialMatch, num]
        else:
            mapping[num] = 1
    return []


# Different way of doing it:
def twoNumberSum(array, target):
    mapping = {}
    for i in range(len(array)):
        num = array[i]
        complement = target - num
        if num in mapping:
            return [mapping[num], num]
        else:
            mapping[complement] = num
    return []


# If asked to return indices instead of nums
def twoNumberSum(array, target):
    mapping = {}
    for i in range(len(array)):
        num = array[i]
        complement = target - num
        if num in mapping:
            return [mapping[num], i]
        else:
            mapping[complement] = i
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoNumberSum(array, target))  # Output: [11, -1]
