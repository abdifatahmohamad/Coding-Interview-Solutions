class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = []
        while nums:
            min_val = min(nums)
            nums.remove(min_val)
            max_val = max(nums)
            nums.remove(max_val)
            avg = (min_val + max_val) / 2
            res.append(avg)

        return len(set(res))
        