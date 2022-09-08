class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        largest = 0
        for n in nums:
            # Check if it's start of the sequence
            if n - 1 not in nums_set:
                length = 0
                while (n + length) in nums_set:
                    length += 1
                largest = max(length, largest)
            
        return largest
        