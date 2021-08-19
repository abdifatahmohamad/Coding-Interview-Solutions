from typing import List


# O(N) Time || O(1) Space
def merge_lists(nums1: List[int], nums2: List[int]) -> List[int]:
    len1, len2 = len(nums1), len(nums2)

    # Create fixed array size for the final return
    new_list = [0] * (len1 + len2)
    # Two pointers (i, j) and k (keep truck the index stored elements)
    i, j, k = 0, 0, 0

    # Edge Case 1: If both arrays are within the range (same length)

    # Traverse both array
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            # arr1 is smaller so we store in the new list
            new_list[k] = nums1[i]
            i += 1
            k += 1
        else:
            # arr2 is smaller so we store in the new list
            new_list[k] = nums2[j]
            j += 1
            k += 1

    # Edge Case 2: If one of the arrays cross the length and the other still remaining:

    # Store remaining elements of arr1
    while i < len1:
        new_list[k] = nums1[i]
        i += 1
        k += 1

    # Store remaining elements of arr2
    while j < len2:
        new_list[k] = nums2[j]
        j += 1
        k += 1

    return new_list


nums1 = [1, 3, 7]
nums2 = [1, 2]

print(merge_lists(nums1, nums2))  # [1, 1, 2, 3, 7]
