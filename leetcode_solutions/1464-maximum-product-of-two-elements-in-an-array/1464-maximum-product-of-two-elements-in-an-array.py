class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        return (-heapq.heappop(heap) - 1) * (-heapq.heappop(heap) - 1)
#
        