class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_dict, count = {}, 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        for num in nums:
            if num + k in nums_dict:
                count += nums_dict[num + k]
        return count

        