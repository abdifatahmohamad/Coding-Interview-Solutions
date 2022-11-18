class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for i in range(len(s)):
            w = list(s[i])
            l, r = 0, len(w) - 1
            while l < r:
                temp = w[l]
                w[l] = w[r]
                w[r] = temp
                l += 1
                r -= 1
            res.append("".join(w))
        return " ".join(res)
