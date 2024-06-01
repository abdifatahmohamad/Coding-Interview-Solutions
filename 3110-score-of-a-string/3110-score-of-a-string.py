class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(char) for char in s]
        
        res = 0
        for i in range(len(ascii_values) - 1):
            res += abs(ascii_values[i] - ascii_values[i + 1])

        return res
        