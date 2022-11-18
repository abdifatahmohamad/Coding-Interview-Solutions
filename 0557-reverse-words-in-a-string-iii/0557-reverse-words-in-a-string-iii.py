class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for i in range(len(s)):
            w = swap(s[i])
            res.append("".join(w))
        return " ".join(res)


def swap(w):
    # word = [w[i] for i in range(len(w))]
    # Short version
    word = list(w)
    l, r = 0, len(word) - 1
    while l < r:
        temp = word[l]
        word[l] = word[r]
        word[r] = temp
        l += 1
        r -= 1
    return "".join(word)
