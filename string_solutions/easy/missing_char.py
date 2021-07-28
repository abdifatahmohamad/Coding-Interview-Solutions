# Test Case 1:
# Input: s = 'kitten'
# Input n = 1
# Output: 'Ktten'

# Test Case 2:
# Input: s = 'kitten'
# Input n = 0
# Output: 'itten'

# Test Case 3:
# Input: s = 'kitten'
# Input n = 4
# Output: 'Kittn'

class Solution:
    def missing_char(self, word: str, index: int) -> str:
        # Solution 1 without loop:
        if index > len(word)-1:
            return ""

        new_list = list(word)
        new_list.pop(index)  # O(N)
        return "".join(new_list)  # O(N)

        # Solution 2 using for loop:
        res = []
        for i in range(len(word)):
            # If curr idx doesn't equal to target idx, don't put in the list
            if i != index:
                res.append(word[i])
        # Return joined list as a string
        return "".join(res)

        # Using string concatenation
        new_list = ""
        for i in range(len(word)):
            if i != index:
                new_list += word[i]
        return new_list


solution = Solution()
print(solution.missing_char('kitten', 1))
