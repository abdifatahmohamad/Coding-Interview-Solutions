# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Initialize left and right pointers
    left = 0
    right = len(array) - 1
    for i in range(len(array)):
        # Already in position, don't swap
        if array[right] == toMove:
            right -= 1

        if array[left] != toMove:
            # It's not the element we wan to swap
            left += 1

        if array[left] == toMove and array[right] != toMove:
            swap(left, right, array)
            # Move pointers together
            left += 1
            right -= 1

    return array


# Swap helper function
def swap(i, j, nums):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
# Output: [4, 1, 3, 2, 2, 2, 2, 2]
print(moveElementToEnd(array, toMove))
