class Solution:
    def countPoints(self, rings: str) -> int:
        mapping = {}
        for i in range(0, len(rings), 2):
            ch = rings[i]
            rod = rings[i + 1]
            if rod not in mapping:
                mapping[rod] = [ch]
            else:
                mapping[rod].append(ch)
        res = 0
        for k, v in mapping.items():
            if len(set(v)) == 3:
                res += 1
        return res
        