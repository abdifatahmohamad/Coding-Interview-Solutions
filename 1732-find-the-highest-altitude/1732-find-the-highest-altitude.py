class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        started_trip = 0 + (gain[0])
        res.append(started_trip)
        for i in range(1, len(gain)):
            alt = started_trip + (gain[i])
            started_trip = alt
            res.append(alt)

        return max(res)
        