class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            # Min-heap
            heapq.heappush(heap, num)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        
        return res
        