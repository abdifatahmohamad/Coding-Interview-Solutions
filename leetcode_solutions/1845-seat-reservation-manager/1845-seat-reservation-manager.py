class SeatManager:
    def __init__(self, n: int):
        self.unres = [num for num in range(1, n + 1)]

    def reserve(self) -> int:
        if not self.unres:
            return -1
        return heapq.heappop(self.unres)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)