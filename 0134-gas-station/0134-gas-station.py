class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diff = [gas[i] - cost[i] for i in range(len(gas))]

        # print(diff)
        total = start = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                start = i + 1
                total = 0
        return start
    
    
        # Short version
        '''
            if sum(gas) < sum(cost):
                return -1

            total = start = 0
            for i in range(len(gas)):
                total += gas[i] - cost[i]
                if total < 0:
                    start = i + 1
                    total = 0
            return start

        '''
        