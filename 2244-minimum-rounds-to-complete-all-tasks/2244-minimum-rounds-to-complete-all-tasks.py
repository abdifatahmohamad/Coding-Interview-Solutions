class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = {}
        for n in tasks:
            frequency[n] = frequency.get(n, 0) + 1

        res = 0
        for n in frequency:
            count = frequency[n]
            if count == 1:
                return -1
            if count % 3 == 0:
                res += count // 3
            if count % 3 == 1 or count % 3 == 2:
                res += count // 3 + 1
        return res
        