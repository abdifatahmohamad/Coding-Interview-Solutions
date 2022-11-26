class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)
        k = 0
        # Traverse from left to right and push
        # all elements which are stricktly less than pivot
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[k] = nums[i]
                k += 1
        
        # Traverse 2nd time from left to right and push
        # all elements which are stricktly equal to pivot
        for i in range(len(nums)):
            if nums[i] == pivot:
                res[k] = nums[i]
                k += 1

        # Traverse 3rd time from left to right and push
        # all elements which are stricktly > to pivot
        for i in range(len(nums)):
            if nums[i] > pivot:
                res[k] = nums[i]
                k += 1
        return res
        