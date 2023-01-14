class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mp = {n: i for i, n in enumerate(nums)}
        
        # This also works
        # mp = Counter(nums)
        missing = []
        for i in range(1, len(nums) + 1):
            if i not in mp:
                missing.append(i)
        return missing
        