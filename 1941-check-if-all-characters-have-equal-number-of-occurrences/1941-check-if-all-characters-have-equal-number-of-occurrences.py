class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mapping = Counter(s)
        values = list(mapping.values())
        for i in range(1, len(values)):
            if values[0] != values[i]:
                return False
        return True
        