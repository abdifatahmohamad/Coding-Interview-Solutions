class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mapping = Counter(s)
        values = []
        for ch in mapping:
            values.append(mapping.get(ch))

        for i in range(1, len(values)):
            if values[i] != values[0]:
                return False
        return True
        