# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        currNum = array[i]
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = currNum + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([currNum, array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 1
# Output: [[-8, 3, 6], [-6, 1, 6], [-6, 2, 5]]
print(threeNumberSum(array, targetSum))
