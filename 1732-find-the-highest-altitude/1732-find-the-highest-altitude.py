class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = float("-inf")
        started_trip = 0 + gain[0]
        max_altitude = max(started_trip, 0)

        for i in range(1, len(gain)):
            alt = started_trip + gain[i]
            started_trip = alt
            max_altitude = max(max_altitude, alt)

        return max_altitude
        