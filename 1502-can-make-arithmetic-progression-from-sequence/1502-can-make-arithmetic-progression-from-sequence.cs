public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        
        Array.Sort(arr);
        int initialDifference = arr[1] - arr[0];
        for(int i = 0; i < arr.Length - 1; i++){
            int currentDifference = arr[i + 1] - arr[i];
            if(currentDifference != initialDifference){
                return false;
            }
        }
        
        return true;
        
    }
}