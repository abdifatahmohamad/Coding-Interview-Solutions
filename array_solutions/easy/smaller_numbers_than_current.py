from typing import List

# Brute force approach using double for loop
# O(N^2) Time || O(N) Space


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
                else:
                    continue
            result.append(counter)

        return result

###########################################################
# Most Optimal Solution - Using sorting ages


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        seen = {}
        for i, num in enumerate(sorted_nums):
            # don't update duplicate in our hash
            if num not in seen:
                seen[num] = i

            # Same as above if statement
            # if age in seen:
            #     continue
            # else:
            #     seen[age] = i

        result = [0] * len(nums)
        for i, num in enumerate(nums):
            result[i] = seen[num]
        return result


solution = Solution()
print(solution.smallerNumbersThanCurrent(
    [7, 2, 1, 2, 3]))  # Output = [4, 1, 0, 1, 3]
# print(solution.smallerNumbersThanCurrent([4, 5, 3, 7])) # Output = [1, 2, 0, 3]
# print(solution.smallerNumbersThanCurrent([5, 5, 5])) # Output = [0, 0, 0]
