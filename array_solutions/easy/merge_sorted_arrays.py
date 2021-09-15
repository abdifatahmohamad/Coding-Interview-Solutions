from typing import List


class Solution:
    @staticmethod
    def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # pointer1 = m -1
        # pointer2 = n - 1
        # nums1_length = m + n
        # index_of_last_element_in_nums1 = m + n -1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge_sorted_array(nums1, n, nums2, m)
    print(nums1)  # [1, 2, 2, 3, 5, 6]
