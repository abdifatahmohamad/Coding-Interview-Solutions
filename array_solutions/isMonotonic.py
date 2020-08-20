# O(n) time | O(1) space
def isMonotonic(array):
    increasing = True
    decreasing = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False

    return increasing or decreasing


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Output: True
print(isMonotonic(array))

