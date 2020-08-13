def twoNumberSum(array, target):
	mapping = {}
	for num in array:
		potentialMatch = target - num
		if potentialMatch in mapping:
			return [potentialMatch, num]
		else:
			mapping[num] = 1
	return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoNumberSum(array, target)) # Output: [11, -1]