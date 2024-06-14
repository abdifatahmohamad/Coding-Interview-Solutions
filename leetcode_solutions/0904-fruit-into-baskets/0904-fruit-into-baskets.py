class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = {}
        left = 0
        right = 0
        max_fruit = float('-inf')
        while right < len(fruits):
            f = fruits[right]
            mapping[f] = mapping.get(f, 0) + 1
            if len(mapping) > 2:
                if mapping[fruits[left]] == 1:
                    del mapping[fruits[left]]
                else:
                    mapping[fruits[left]] -= 1
                left += 1
            
            max_fruit = max(max_fruit, right - left + 1)
            right += 1
        return max_fruit
    
    def totalFruitForLoop(self, fruits: List[int]) -> int:
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
        