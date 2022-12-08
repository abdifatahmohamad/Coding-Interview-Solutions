class Solution:
    def breakPalindrome(self, s: str) -> str:
        s = list(s)
        if len(s) == 1:
            return ""
        for i in range(len(s) // 2):
            if s[i] > 'a':
                s[i] = 'a'
                break
                
        else:
            s[-1] = 'b'

        return "".join(s)
      