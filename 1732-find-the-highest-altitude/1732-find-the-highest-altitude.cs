public class Solution {
    public int LargestAltitude(int[] gain) {
        List<int> list = new List<int>();
        list.Add(0);
        int startedTrip = 0 + (gain[0]);
        list.Add(startedTrip);
        for(int i = 1; i < gain.Length; i++){
            int altitude = startedTrip + (gain[i]);
            startedTrip = altitude;
            list.Add(altitude);
        }
        
        return list.Max();
        
    }
}