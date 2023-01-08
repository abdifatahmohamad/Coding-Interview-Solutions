class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = {}
        for n in tasks:
            frequency[n] = frequency.get(n, 0) + 1

        res = 0
        for key, value in frequency.items():
            if value == 1:
                return -1
            if value % 3 == 0:
                res += value // 3
            if value % 3 == 1 or value % 3 == 2:
                res += value // 3 + 1
        return res
        