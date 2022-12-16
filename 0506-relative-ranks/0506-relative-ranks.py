class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        d = {}
        ranking = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, n in enumerate(s):
            if i < len(ranking):
                d[n] = ranking[i]
            else:
                d[n] = str(i + 1)
                
        res = [d.get(s)  for s in score]
        return res