class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapping = {}
        res = []
        for i, groupSize in enumerate(groupSizes):
            # Use ith index as a person
            person = i
            if groupSize not in mapping:
                mapping[groupSize] = []
            mapping.get(groupSize).append(person)
            key = mapping.get(groupSize)
            if len(key) == groupSize:
                res.append(key)
                # Remove key
                del mapping[groupSize]
        return res
        