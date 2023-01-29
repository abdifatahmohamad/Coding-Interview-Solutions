class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(names)):
            mapping[heights[i]] = names[i]

        mapping = sorted(mapping.items(), reverse=True)
        res = []
        for _, people in mapping:
            res.append(people)
        return res
        