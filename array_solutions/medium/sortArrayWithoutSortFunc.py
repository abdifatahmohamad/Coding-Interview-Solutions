from typing import List

# Sort Colors - LeetCode


class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        start, current, end = 0, 0, len(nums) - 1

        while current <= end:
            if nums[current] == 0:
                self.swap(nums, current, start)
                current += 1
                start += 1
            elif nums[current] == 2:
                self.swap(nums, current, end)
                end -= 1
            else:
                current += 1
        return nums

    # Using helper function to swap the values
    @staticmethod
    def swap(nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

###########################################################################


class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        start, current, end = 0, 0, len(nums) - 1

        while current <= end:
            if nums[current] == 0:
                # temp = nums[current]
                # nums[current] = nums[start]
                # nums[start] = temp

                # Same as above swap technique but in one line
                nums[current], nums[start] = nums[start], nums[current]

                current += 1
                start += 1
            elif nums[current] == 2:
                # temp = nums[current]
                # nums[current] = nums[end]
                # nums[end] = temp

                # Same as above swap technique but in one line
                nums[current], nums[end] = nums[end], nums[current]

                end -= 1
            else:
                current += 1
        return nums


solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
print(solution.sortColors(nums))  # Output: [0, 0, 1, 1, 2, 2]
