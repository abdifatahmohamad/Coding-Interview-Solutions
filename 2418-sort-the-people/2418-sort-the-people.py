class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(names)):
            mapping[heights[i]] = names[i]
        res = []
        for _, people in sorted(mapping.items(), reverse=True):
            res.append(people)
        return res
        