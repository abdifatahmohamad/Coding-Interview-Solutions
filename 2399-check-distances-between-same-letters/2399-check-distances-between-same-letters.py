class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mapping = {}
        for i, c in enumerate(s):
            if c not in mapping:
                mapping[c] = [i]
            else:
                mapping[c].append(i)
        
        print(mapping)
        for k, v in mapping.items():
            if (abs(v[0] - v[1]) - 1) != distance[ord(k) - ord('a')]:
                return False

        return True
        