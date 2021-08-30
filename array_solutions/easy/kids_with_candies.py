from typing import List


class Solution:
    def kids_with_candies(self, nums: List[int], extra_money: int) -> List[bool]:
        # Set fixed list size
        result = [False] * len(nums)

        # Find max number using for loop:
        max_num = 0
        for num in nums:
            if num > max_num:
                max_num = num

        for i, num in enumerate(nums):
            if num + extra_money >= max_num:
                result[i] = True
        return result


        # Same as above
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     diff = max_num - extra_money
        #     if curr >= diff:
        #         result[i] = True
        # return result


solution = Solution()
# Output = [True, True, True, False, True, False, True]
print(solution.amused_runny_sales([6, 7, 5, 3, 9, 4, 8], 4))
# Output = [True, False, True, True, True]
print(solution.amused_runny_sales([2, 1, 5, 3, 4], 3))
