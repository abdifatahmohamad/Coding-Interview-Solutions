from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1Idx = {n:i for i, n in enumerate(nums1)}

        d = {}
        for idx, num in enumerate(nums1):
            d[num] = idx

        ans = [-1] * (len(nums1))
        for i in range(len(nums2)):
            if nums2[i] not in d:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = d[nums2[i]]
                    ans[idx] = nums2[j]
                    break
        return ans


solution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

# Output: [-1,3,-1]

print(solution.nextGreaterElement(nums1, nums2))
