class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mapping = Counter(jewels)
        # mapping = {}
        # for j in jewels:
        #     mapping[j] = mapping.get(j, 0) + 1

        res = 0
        for s in stones:
            if s in mapping:
                res += 1
        return res
        