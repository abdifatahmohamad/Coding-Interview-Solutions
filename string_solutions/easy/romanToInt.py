class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i in range(len(s)):
            # i + 1 < len(s) checks if next value is in bounds (range)
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res


solution = Solution()
# string = "III"
# string = "MCMXCIV"
# string = "LVIII"
string = "MCMXCVI"    # ---> Output: 1996
print(solution.romanToInt(string))
