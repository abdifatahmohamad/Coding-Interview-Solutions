class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            if n != 0:
                heapq.heappush(heap, n)
        res = 0
        while heap:
            smallest_non_zero = heapq.heappop(heap)
            while heap and smallest_non_zero == heap[0]:
                heapq.heappop(heap)
            res += 1
            for i in range(len(heap)):
                heap[i] -= smallest_non_zero

        return res
