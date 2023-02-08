class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:len(nums) // 2]
        arr2 = nums[len(nums) // 2:]

        res = []
        i = 0
        while i < n:
            res.append(arr1[i])
            res.append(arr2[i])
            i += 1
        return res 
        