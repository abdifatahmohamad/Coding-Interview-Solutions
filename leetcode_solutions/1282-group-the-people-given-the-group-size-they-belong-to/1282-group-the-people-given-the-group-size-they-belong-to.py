class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mapping = {}
        res = []
        for i, groupSize in enumerate(groupSizes):
            # Use ith index as a person
            person = i
            if groupSize not in mapping:
                mapping[groupSize] = []
                
            value = mapping.get(groupSize)
            value.append(person)
        
            if len(value) == groupSize:
                res.append(value)
                # Remove key
                del mapping[groupSize]
        return res
        