class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for s in score:
            heapq.heappush(heap, -s)
        
        d = {}
        ranking = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, n in enumerate(score):
            s = heapq.heappop(heap) * -1
            if i < len(ranking):
                d[s] = ranking[i]
            else:
                d[s] = str(i + 1)
        
        res = [d.get(s) for s in score]
        return res