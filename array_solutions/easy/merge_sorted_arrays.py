from typing import List


class Solution:
    @staticmethod
    def merge_sorted_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # https://www.youtube.com/watch?v=P1Ic85RarKY

        # pointer1 = m -1 # --> array index starts at 0
        # pointer2 = n - 1 # --> array index starts at 0
        # nums1_length = m + n
        # index_of_last_element_in_nums1 = m + n -1

        last = len(nums1) - 1  # or lest = m + n -1

        # Traverse both array in reverse
        while m > 0 and n > 0:
            # Case 1:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            # Case 2: if nums2[n] > nums1[m] or nums2[n] > nums1[m]
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        # Case 3: fill nums1 array with leftover nums2 array
        while n > 0:
            nums1[last] = nums2[n - 1]
            # Decrement both last and n pointers in one line
            last, n = last - 1, n - 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge_sorted_array(nums1, n, nums2, m)
    print(nums1)  # [1, 2, 2, 3, 5, 6]
