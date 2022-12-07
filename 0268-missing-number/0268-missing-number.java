class Solution {
    public int missingNumber(int[] nums) {
        // Map<Integer, Integer> mp = new HashMap<>();
        // for (int i = 0; i < nums; i++){
        //     if (mp.containsKey(arr[i]))
        //     {
        //         mp.put(arr[i], mp.get(arr[i]) + 1);
        //     }
        //     else
        //     {
        //         mp.put(arr[i], 1);
        //     }
        // }
        
        // Shorter version
        Map<Integer,Integer> mp = new HashMap<>();
        for(int n: nums){
           mp.put(n, mp.getOrDefault(n, 0) + 1);
        }
        
        int missing = 0;
        for(int i = 1; i < nums.length + 1; i++){
            if(!mp.containsKey(i)){
                missing = i;
            }
        }
        // for i in range(1, len(nums) + 1):
        //     if i not in lookup:
        //         missing = i

        return missing;
        
    }
}