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
