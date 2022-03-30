from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                mapping[nums2[idx]] = nums2[i]
            stack.append(i)

        # res = [0] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in mapping:
                # res[i] = mapping[nums1[i]]
                nums1[i] = mapping[nums1[i]]
            else:
                # res[i] = -1
                nums1[i] = -1

        # return res
        return nums1


solution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

# Output: [-1,3,-1]

print(solution.nextGreaterElement(nums1, nums2))
