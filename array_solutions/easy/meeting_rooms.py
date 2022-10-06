from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def meeting_rooms(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev.end > curr.start:
                return False
        return True


intervals1 = [Interval(5, 10), Interval(15, 20), Interval(0, 30)]
intervals2 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
intervals3 = [Interval(5, 8), Interval(9, 15)]

solution = Solution()

print(solution.meeting_rooms(intervals1))
print(solution.meeting_rooms(intervals2))
print(solution.meeting_rooms(intervals3))


# Unit testing
def test():
    assert solution.meeting_rooms(
        [Interval(5, 10), Interval(15, 20), Interval(0, 30)]) == False
    assert solution.meeting_rooms(
        [Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == False
    assert solution.meeting_rooms([Interval(5, 8), Interval(9, 15)]) == True
