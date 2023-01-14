class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort(key=lambda x: x[1])
        points = sorted(points, key=lambda x: x[1])
        res = 0
        prevoius = float("-Inf")
        for point in points:
            start, end = point[0], point[1]
            if start > prevoius:
                res += 1
                prevoius = end

        return res
        