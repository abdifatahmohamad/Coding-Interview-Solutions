from typing import List


# Testing program
def findMergeArr(arr1: List[int], arr2: List[int]) -> int:
    i, j = 0, 0
    # Traverse array simultaneously
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        else:
            break
    return arr1[i]


arr1 = [1, 2, 3]
arr2 = [1, 3]
print(findMergeArr(arr1, arr2))
