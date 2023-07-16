class Solution {
    public List<Integer> partitionLabels(String s) {
        char[] chars = s.toCharArray();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < chars.length; i++) {
            map.put(String.valueOf(chars[i]), i);
            // map.put(chars[i] + "", i);
        }
        
        // for (Map.Entry<String, Integer> entry : map.entrySet()) {
        //     String key = entry.getKey();
        //     int value = entry.getValue();
        //     System.out.println(key + ":" + value);
        // }
        
        List<Integer> res = new ArrayList<>();
        int size = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            // Retrieve character from s
            char ch = s.charAt(i); 
            // Retrieve key from map
            String key = String.valueOf(ch); 
            // Retrieve last index from map
            int lastIndex = map.get(key); 

            // System.out.println("Character: " + ch + 
            //                    ", Index: " + i + 
            //                    ", Key: " + key + 
            //                    ", Last Index: " + lastIndex);
            
            // As soon as we see a character, update the size of partition
            size++;
            // Update the end of the partition 
            // if last index of map of curr char from map > current ennd
            // if(lastIndex > end){
            //     // Update that curr end to last index of curr character from map
            //     end = lastIndex;
            // }
            // Similar above if:
            end = Math.max(end, lastIndex);
            // Stop partition if we reach the end of partition
            if(i == end){
                // Add the size to the result
                res.add(size);
                // Set size to zero to start new partition
                size = 0;
            }   
        }  
        return res;
    }
}