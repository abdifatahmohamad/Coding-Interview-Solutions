class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [0 for i in range(len(s) +  1)]
        # res = [0] * int(len(s) +  1)
        low, high = 0, len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                res[i] = low
                low += 1
            else:
                res[i] = high
                high -= 1
        res[len(s)] = high
        return res
        