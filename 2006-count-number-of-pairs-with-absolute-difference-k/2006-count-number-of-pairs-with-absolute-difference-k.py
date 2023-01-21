class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mapping = Counter(nums)

        count = 0
        for n in nums:
            complement = n + k
            if complement in mapping:
                count += mapping[complement]
        return count


'''
mapping = {
    3: 1,
    2: 1,
    1: 1,
    5: 1,
    4: 1
}

count = 0
k = 2
nums = [3, 2, 1, 5, 4]
complement = 3 + 2 in mapping ==> yes
mapping[complement] = 1
count += mapping[complement]
count = 1


complement = 2 + 2 in mapping ==> yes
count += mapping[complement]
count = 2


complement = 1 + 2 in mapping ==> yes
count += mapping[complement]
count = 3


complement = 5 + 2 in mapping ==> no

complement = 4 + 2 in mapping ==> no

return count
'''