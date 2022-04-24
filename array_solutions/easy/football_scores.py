# Brute force solution:
from bisect import bisect_right  # For binary search.


def counts(teamA, teamB):
    res = []
    for b in teamB:
        count = 0
        for a in teamA:
            count += a <= b
        res.append(count)
    return res


# Short version using list comprehension:
[sum(lst1 <= lst2 for lst1 in teamA) for lst2 in teamB]


# O(NLOGN) Time || O(N) Space
def counts(teamA, teamB):
    lst1_sorted = sorted(teamA)
    '''
    res = []
    for val in teamB:
        res.append(binary_search(lst1_sorted, val))
    return res
    '''
    # Short version with list comprehension
    return [binary_search(lst1_sorted, val) for val in teamB]


def binary_search(nums, val):
    left, right = 0, len(nums)
    while left < right:
        mid = (right + left) // 2
        if nums[mid] <= val:
            left = mid + 1
        else:
            right = mid

    return right


print(counts([1, 2, 3], [2, 4]))
print(counts([1, 4, 2, 4], [3, 5]))  # [2, 4]
print(counts([2, 10, 5, 4, 8], [3, 1, 7, 8]))  # [1, 0, 3, 4]


# Using bisect_right imported from binary search package
lst1_sorted = sorted(teamA)  # NlogN

res = [bisect_right(lst1_sorted, val) for val in teamB]  # MlogN
