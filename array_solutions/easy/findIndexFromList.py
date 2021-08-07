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

################################################


def print_from_last(arr: List[str], pos) -> str:
    if pos > len(arr) - 1:
        return "Invalid Position."

    k = 0
    length = len(arr) - 1 - pos
    while length > 0:
        length -= 1
        k += 1
    return arr[k]


arr = ["MSP", "BOS", "ATL", "LAX"]
pos = 3

print(print_from_last(arr, pos))

################################################
# O(1) Time and Space


def PFL(arr: List[str], pos) -> str:
    if pos > len(arr) - 1:
        return "Invalid Position"
    return arr[len(arr) - 1 - pos]


arr = ["MSP", "BOS", "ATL", "LAX"]
pos = 3
print(PFL(arr, pos))
