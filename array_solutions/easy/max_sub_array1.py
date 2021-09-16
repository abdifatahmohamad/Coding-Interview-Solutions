import time
from typing import List


class Solution:
    @staticmethod
    # def max_sub_array(nums: List[int]) -> float:
    #     max_sum = float('-inf')
    #     n = len(nums)
    #     for right in range(n):
    #         running_sum = 0
    #         for left in range(right, n):
    #             running_sum += nums[left]
    #             max_sum = max(max_sum, running_sum)
    #     return max_sum
    def max_sub_array(nums: List[int]) -> float:
        print("########################### Brute Force Solution ############################# ")
        start_time = time.time()
        max_sum = float('-inf')
        n = len(nums)
        for left in range(n):
            current_sum = 0
            for right in range(left, n):
                current_sum += nums[right]
                if current_sum > max_sum:
                    max_sum = current_sum

        end_time = time.time()
        print(f"Start time: {start_time}, \nEnd time: {end_time}")
        time_taken = end_time - start_time
        print(f"Total execution time: {time_taken} seconds")
        print(max_sum)

        print("\n########################### Optimized Solution ############################# ")
        start_time = time.time()
        max_sum = float('-inf')
        n = len(nums)
        current_sum = 0
        for i in range(n):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        end_time = time.time()
        print(f"Start time: {start_time}, \nEnd time: {end_time}")
        time_taken = end_time - start_time
        print(f"Total execution time: {time_taken} seconds")
        print(max_sum)

        #############################################################
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

        return max_sum


if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Output: sum of : 4, -1, 2, 1 = 6
    # nums2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.max_sub_array(nums))
