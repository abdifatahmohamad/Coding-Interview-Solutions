class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        j = 0
        for i in range(len(nums)):
            # nums[j] gives us some kind of index
            ans[i] = nums[nums[j]]
            j += 1

        return ans
        