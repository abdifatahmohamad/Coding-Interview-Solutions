class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        mapping = collections.Counter(nums)
        unique = 0
        res = []
        for n in nums: 
            complement1 = n - diff
            complement2 = n + diff 
            curr = n 
            if complement1 in mapping and complement2 in mapping:
                res.append((complement1, curr, complement2))
                unique += 1
        print(res)
        return unique