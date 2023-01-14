def kth_from_beginning(nums, k):
  if k > len(nums):
    return None

  return nums[k - 1]


def kth_from_end(nums, k):
  if not nums or k > len(nums):
    return None

  return nums[len(nums) - k]


nums = [1, 9, 3, 6, 5]
k = 2
print(kth_from_beginning(nums, k)) # 9
print(kth_from_end(nums, k)) # 6
