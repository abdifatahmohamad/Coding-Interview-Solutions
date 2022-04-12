def removeElement(nums, val):
    idx = 0
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            temp = nums[idx]
            nums[idx] = nums[i]
            nums[i] = temp
            idx += 1
            k += 1

    return k


# Less code same solution
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# Two pointers solution
def removeElement(nums, val):
    left, right = 0, len(nums) - 1
    k = 0
    while left <= right:
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
            k += 1
    return k


# print(removeElement([3, 2, 2, 3], 3))  # Output: 2, nums = [2,2,_,_]
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
# Output: 5, nums = [0,1,4,0,3,_,_,_]
