from typing import List


class Solution:
    def moveZerosToFront(self, nums: List[int]) -> List[int]:
        if nums == 0:
            return []
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                self.swap(idx, i, nums)
                idx += 1
        return nums

    @staticmethod
    def swap(i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    # Using while loop:
     def moveZerosToFront(self, nums: List[int]) -> List[int]:
        if nums == 0:
            return []
        idx = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                self.swap(idx, i, nums)
                idx += 1
            i += 1
        return nums


    @staticmethod
    def swap(i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


solution = Solution()
nums = [12, 1, 0, 3, 0]
print(solution.moveZerosToFront(nums))  # Output: [0, 0, 1, 3, 12]

# Input: nums = [0]
# Output: [0]
