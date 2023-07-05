class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {n: i for i, n in enumerate(arr2)}
        arr1.sort(key=lambda val: custom_sort(val, mp, arr2))
        return arr1


def custom_sort(val, mp, arr2):
    if val in mp:
        return mp[val]
    else:
        return len(arr2) + val
        