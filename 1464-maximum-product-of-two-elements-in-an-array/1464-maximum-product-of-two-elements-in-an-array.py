class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        max_val1 = -heapq.heappop(heap)
        max_val2 = -heapq.heappop(heap)

        return (max_val1 - 1) * (max_val2 - 1)
#
        