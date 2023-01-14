class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequency = {}
        for n in tasks:
            frequency[n] = frequency.get(n, 0) + 1

        count = 0
        for key, value in frequency.items():
            if value == 1:
                return -1
            else:
                count += value // 3
                if value % 3 != 0:
                    count += 1
        
        return count
        