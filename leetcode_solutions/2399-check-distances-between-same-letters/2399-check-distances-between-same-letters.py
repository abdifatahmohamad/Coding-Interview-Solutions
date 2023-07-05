class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mapping = {}
        for i, c in enumerate(s):
            if c in mapping:
                mapping[c] = i - mapping.get(c) - 1
            else:
                mapping[c] = i
        
        for k in mapping:
            if mapping.get(k) != distance[ord(k) - ord('a')]:
                return False

        return True
        