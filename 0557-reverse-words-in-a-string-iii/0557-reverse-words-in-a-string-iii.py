class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        res = ""
        for i in range(len(st)):
            st[i] = swap(st[i])
        return " ".join(st)
            
def swap(word):
    w = list(word)
    l, r = 0, len(w) - 1
    while l < r:
        w[l], w[r] = w[r], w[l]
        l += 1
        r -= 1
    return "".join(w)
