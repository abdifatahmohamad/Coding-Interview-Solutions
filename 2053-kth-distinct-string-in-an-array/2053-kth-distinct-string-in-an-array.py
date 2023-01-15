class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = Counter(arr)
        res = 0
        for ch in distinct:
            if distinct.get(ch) == 1:
                res += 1
            if res == k:
                return ch
        return ""
            
        