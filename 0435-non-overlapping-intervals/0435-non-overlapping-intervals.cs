public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        int end = int.MinValue;
        int res = 0;
        // var points = intervals.OrderBy(x => x[1]);
        Array.Sort(intervals, (x, y) => x[1].CompareTo(y[1]));
        foreach (int[] arr in intervals){
            if (arr[0] >= end){
                end = arr[1];
            } else{
                res++;
            }
        }
        
        return res;
    }
}