class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappushpop(heap, n) if len(heap) >= k else heapq.heappush(heap, n)
                
        return heap[0]