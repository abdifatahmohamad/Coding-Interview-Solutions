from typing import List


def findIndexFromLast(arr: List[str], targetIdx) -> str:
    k = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        # k = 3
        if i == (k - targetIdx):
            return arr[i]
    if targetIdx > len(arr) - 1:
        return "Invalid Position."


arr = ["MSP", "BOS", "ATL", "LAX"]
targetIdx = 3

print(findIndexFromLast(arr, targetIdx))
