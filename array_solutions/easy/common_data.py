from typing import List


class Solution:
    def match_words(self, list1: List[int], list2: List[int]) -> List[int]:
        seen = {}
        for num in list1:
            seen[num] = seen.get(num, 0) + 1
        for el in list2:
            if el in seen:
                return True
        return None

        # Another solution:
        # for num in list2:
        #     if num in list1:
        #         return True
        # return None

        # Same above code using list comprehension
        # return None if [num for num in list2 if num in list1] == [] else True


solution = Solution()
print(solution.match_words([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))  # True
print(solution.match_words([1, 2, 3, 4, 5], [6, 7, 8, 9]))  # None
