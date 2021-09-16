# Maximum Sub Array Leetcode #53 Problem
# nums = [-1, 2, -3, 4, 5]
# max_sum = float('-inf')
# current_sum = 0
# for i in range(len(nums)):
#     # It gives the maximum sum of up to the current element we sitting on
#     current_sum += nums[i]
#     # print(f"Index: {i}, current value: {current_sum}")
#     if current_sum > max_sum:
#         max_sum = current_sum
#     # Reset
#     if current_sum < 0:
#         current_sum = 0
#     # print(current_sum)
# print(max_sum)

# (-1) = -1
# (-1) + 2 = 1
# 1 + (-3) = -2
# (-2) + 4 = 2
# 2 + 5 = 7


# A way to know the max sum array of current element
# nums = [1, 2, 3, 4, 5]
# max_sum = float('-inf')
# current_sum = 0
# for i in range(len(nums)):
#     current_sum += nums[i]
#     print(current_sum)

# 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 +  4 = 10
# 10 + 5  = 15


nums = [-1, 2, -3, 4, 5]
max_sum = nums[0]
current_sum = max_sum
for i in range(1, len(nums)):
    current_sum = max(nums[i] + current_sum, nums[i])
    # current_sum iterations:
    # (2 + (-1), 2 ) = (1, 2) -> max(1, 2) = 2
    # ((-3) + 2, -3) = (-1, -3) -> max(-1, -3) = -12 -1 4 9
    # (4 + (-3), 4 ) = (1, 4) -> max(1, 4) = 4
    # (5 + 4, 5) = (9, 5) -> max(9, 5) = 9
    # current_sum = 2, -1, 4, 9
    max_sum = max(current_sum, max_sum)
    # max_sum iterations:
    # max(2, -1) = 2
    # max(-1, -1) = -1
    # max(4, -1) = 4
    # max(9, -1) = 9
    # In this case 9 is the max_sum we finally have

print(max_sum)
