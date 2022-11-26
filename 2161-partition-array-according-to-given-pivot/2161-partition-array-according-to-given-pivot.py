class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[k] = nums[i]
                k += 1

        for i in range(len(nums)):
            if nums[i] == pivot:
                res[k] = nums[i]
                k += 1

        for i in range(len(nums)):
            if nums[i] > pivot:
                res[k] = nums[i]
                k += 1
        return res
        