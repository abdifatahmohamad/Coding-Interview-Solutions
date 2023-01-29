class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCounts = [0 for _ in range(n + 1)]
        for p1, p2 in trust:
            trustCounts[p1] -= 1
            trustCounts[p2] += 1
            
        for i in range(1, len(trustCounts)):
            if trustCounts[i] == n - 1:
                return i
        return -1
        