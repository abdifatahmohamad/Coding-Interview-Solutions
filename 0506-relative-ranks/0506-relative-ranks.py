class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        mapping = {}
        ranking = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, n in enumerate(s):
            if i < len(ranking):
                mapping[n] = ranking[i]
            else:
                mapping[n] = str(i + 1)

        res = [mapping.get(s) for s in score]   
        return res
        

            
            
            
        
  