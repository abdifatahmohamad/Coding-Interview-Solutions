class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [0 for i in range(len(s) +  1)]
        # res = [0] * int(len(s) +  1)
        low, high = 0, len(s)
        i = k = 0
        while i < len(s):
            if s[i] == 'I':
                res[k] = low
                low += 1
            else:
                res[k] = high
                high -= 1
            k += 1
            i += 1
            
        # res[len(s)] = high
        if s[-1] == 'I':
            res[k] = low
        else:
            res[k] = high
            
        return res
        