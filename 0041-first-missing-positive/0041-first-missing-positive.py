class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_set = set()
    
        # Iterate through the input array and add each positive integer to the set
        for num in nums:
            if num > 0:
                positive_set.add(num)

        # The first missing positive integer is the smallest positive integer that is not in the set
        i = 1
        while i in positive_set:
            i += 1

        return i
