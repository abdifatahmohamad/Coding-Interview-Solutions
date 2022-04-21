
# Using STACK data structures
def merge(nums1, nums2):
    mergedArr = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            mergedArr.append(nums1.pop(0))
        else:
            mergedArr.append(nums2.pop(0))
    # The remaining elements of the list will be appended to the final list.
    mergedArr += nums1
    mergedArr += nums2

    return mergedArr


print(merge([1, 2, 3], [2, 3, 5]))
