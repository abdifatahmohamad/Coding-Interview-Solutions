from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i in nums1:
            # mapping[i] = mapping.get(i, 0) + 1
            mapping[i] = True

        res = []
        for j in nums2:
            if j in mapping and j not in res:
                res.append(j)
        return res

        # res = []
        # for j in nums2:
        #     if j in mapping and mapping[j] > 0:
        #         res.append(j)
        #         mapping[j] = 0
        # return res


solution = Solution()

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2))
