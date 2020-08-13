def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	i = j = 0
	smalllest = current = float("inf")
	smallestPair = []
	while i < len(arrayOne) and j < len(arrayTwo):
		firstNum, secondNum = arrayOne[i], arrayTwo[j]
		current = abs(firstNum - secondNum)
		if firstNum < secondNum:
			# current = secondNum - firstNum
			i += 1
		elif secondNum < firstNum:
			# current = firstNum - secondNum
			j += 1
		else:
			return [firstNum, secondNum]
		if smalllest > current:
			smalllest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo)) #Output: [28, 26]