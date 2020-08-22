# O(n) time | O(1) space
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for word in range(len(s) - 1, -1, -1):
            res.append(s[word])
        return " ".join(res)


# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        word = list(s)
        left, right = 0, len(word) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return " ".join(s)


solution = Solution()
print(solution.reverseWords("the sky is blue"))
# Output: "blue is sky the"
