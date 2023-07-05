class Solution {
    public int singleNumber(int[] nums) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        // Normal check keys and values
        // for(Integer n : nums){
        //     if(map.containsKey(n)){
        //         map.put(n, map.get(n) + 1);
        //     } else{
        //         map.put(n, 1);
        //     }
        // }
        
        // Using computeIfPresent
//         for (Integer n : nums) {
//             if (!map.containsKey(n)) {
//                 map.put(n, 1);

//             } else {
//                 map.computeIfPresent(n,
//                         (key, val) -> val + 1);
//             }
//         }
        
        // Preferred version and shortcut using getOrDefault
        for(Integer n : nums){
            map.put(n, map.getOrDefault(n, 0) +  1);
        }
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            
            if(value == 1){
                return key;
            }
        }
        
        return -1;
        
    }
}