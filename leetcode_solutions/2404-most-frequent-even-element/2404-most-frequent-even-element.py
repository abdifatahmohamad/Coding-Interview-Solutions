class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mapping = {}
        most_frequent = float("-Inf")
        res = float("inf")
        for n in nums:
            if n % 2 == 0:
                mapping[n] = mapping.get(n, 0) + 1
                if mapping.get(n) >= most_frequent:
                    if most_frequent < mapping.get(n):
                        res = n
                    else:
                        res = min(res, n)
                    most_frequent = mapping[n]
        return -1 if res == float("inf") else res
        