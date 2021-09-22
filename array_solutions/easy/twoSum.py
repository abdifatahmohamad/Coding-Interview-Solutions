# O(N^2) Time, O(1) Space
def twoNumberSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
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
def sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in seen:
            seen[nums[i]] = i
        else:
            return [seen[complement], i]
    return seen


print(sum([2, 15, 11, 7], 9))

# Complement = target - num
# 9 - 2 = 7 -> is 7 in seen => NO, store 2 in hashmap
# 9 - 15 = -6 -> is -6 in seen => NO, store 15 in hashmap
# 9 - 11 = -2 -> is -2 in seen => NO, store 11 in hashmap
# 9 - 7 = 2 -> is 2 in seen => YES, return it its index in hashmap and the index of nums[i]

# seen = {
# 2 = 0
# 15  = 1
# 11 - 2
# }

# Loop through till the end of numbers array
# determine complement
# if complement is in dictionary, return value of complement and i
# otherwise, new key-value pair in dicitonary, number -> i


array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoNumberSum(array, target))  # Output: [11, -1]
