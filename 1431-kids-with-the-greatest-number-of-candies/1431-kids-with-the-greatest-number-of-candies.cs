public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        
        bool[] result = new bool[candies.Length];
        
        int maxNum = 0;
        foreach(int num in candies){
            if (num > maxNum){
                maxNum = num;
            }
        }
        
        for(int i=0; i<candies.Length; i++){
            if(candies[i] + extraCandies >= maxNum){
                result[i] = true;
            }
        }
        
        return result;
        
    }
}