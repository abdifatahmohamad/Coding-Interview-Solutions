class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        max_length = 0
        count = 0
        for i in range(len(nums)):
            # if nums[i]:
            #     count += 1
            # else:
            #     count -= 1

            # Short version
            count += (1 if nums[i] == 1 else -1)

            if count in d:
                max_length = max(max_length, (i - d[count]))
            else:
                d[count] = i
        return max_length
        