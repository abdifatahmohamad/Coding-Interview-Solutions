class Solution:
    def scoreOfString(self, s: str) -> int:
        bucket = [0 for _ in range(26)]
    
        indices = []
        for char in s:
            index = ord(char) - ord('a')
            indices.append(index)

        res = 0
        for i in range(len(indices) - 1):
            res += abs(indices[i] - indices[i + 1])

        return res
        