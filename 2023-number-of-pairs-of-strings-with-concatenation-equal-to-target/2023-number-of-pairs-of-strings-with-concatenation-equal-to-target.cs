public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        
        int res = 0;
        for(int i=0; i < nums.Length; i++){
            for(int j=0; j < nums.Length; j++){
                if(i == j){
                    continue;
                }
                
                if(nums[i] + nums[j] == target){
                    res ++;
                }
            }
        }
        
        return res;
        
    }
}