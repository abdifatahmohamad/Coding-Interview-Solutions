class Solution:
    def countPoints(self, rings: str) -> int:
        mapping = {}
        for i in range(len(rings)):
            char = rings[i]
            if char.isalpha():
                rods = rings[i + 1]
                if rods not in mapping:
                    mapping[rods] = [char]
                else:
                    mapping[rods].append(char)

        colors = ['R', 'G', 'B']
        res = 0
        for i, rods in mapping.items():
            if set(rods) == set(colors):
                res += 1
        return res
        