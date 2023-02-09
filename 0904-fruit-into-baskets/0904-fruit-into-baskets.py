class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = {}
        l = 0
        res = float('-inf')
        for r, f in enumerate(fruits):
            mapping[f] = mapping.get(f, 0) + 1
            if len(mapping) > 2:
                if mapping[fruits[l]] == 1: 
                    del mapping[fruits[l]]
                else: 
                    mapping[fruits[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        