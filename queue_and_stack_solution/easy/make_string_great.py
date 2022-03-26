class Solution:
    def makeGood(self, s: str) -> str:

        # Case 1:
        if len(s) == 1:
            return s

        stack = []
        for ch in s:
            stack.append(ch)

            if len(stack) >= 2 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()

        return "".join(stack)


solution = Solution()
# Test Case 1
# s = "leEeetcode"
# Output: "leetcode"

# Test Case 2
s = "abBAcC"
# Output: ""

# Test Case 3
# s = "s"
# Output: "s"
print(solution.makeGood(s))
