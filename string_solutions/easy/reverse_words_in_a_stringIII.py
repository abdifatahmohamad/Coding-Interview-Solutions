# O(n) time | O(1) space
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i, word in enumerate(s):
            s[i] = self.helper(word)
        return " ".join(s)

    @staticmethod
    def helper(word):
        word = list(word)
        left, right = 0, len(word) - 1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return "".join(word)


# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) < 1:
            return ""

        s = s.split()
        res = []
        for word in s:
            res.append(word[::-1])
        return " ".join(res)


solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
# Output: "s'teL ekat edoCteeL tsetnoc"
