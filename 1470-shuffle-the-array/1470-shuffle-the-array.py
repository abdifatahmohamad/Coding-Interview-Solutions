class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            curr_first_half = nums[i]
            curr_2nd_half = nums[n + i]
            res.append(curr_first_half)
            res.append(curr_2nd_half)
            
        return res
        