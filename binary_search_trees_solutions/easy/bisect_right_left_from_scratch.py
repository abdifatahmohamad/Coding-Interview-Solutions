class Solution(object):
    def bisectLeft(self, nums, target):
        """
        Returns leftmost insertion point that target should be inserted in the sorted array
        """
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def bisectRight(self, nums, target):
        """
        Returns rightmost insertion point that target should be inserted in the sorted array
        """
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        left_bound = self.bisectLeft(nums, target)  # O(logN)
        right_bound = self.bisectRight(nums, target)  # O(logN)

        return [left_bound, right_bound - 1] if left_bound != right_bound else [-1, -1]
