class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort(key=lambda x: x[1])
        points = sorted(points, key=lambda x: x[1])
        res = 0
        ending = float("-Inf")
        for point in points:
            start, end = point[0], point[1]
            if start > ending:
                res += 1
                ending = end

        return res
        