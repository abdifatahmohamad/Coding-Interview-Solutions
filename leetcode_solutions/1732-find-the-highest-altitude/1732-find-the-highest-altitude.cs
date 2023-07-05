public class Solution {
    public int LargestAltitude(int[] gain) {
        int max_altitude = int.MinValue;
        int started_trip = 0 + gain[0];
        max_altitude = Math.Max(started_trip, 0);

        for (int i = 1; i < gain.Length; i++)
        {
            int alt = started_trip + gain[i];
            started_trip = alt;
            max_altitude = Math.Max(max_altitude, alt);
        }

        return max_altitude;
        
    }
}