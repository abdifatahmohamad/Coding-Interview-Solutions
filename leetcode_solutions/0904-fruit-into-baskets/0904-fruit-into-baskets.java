class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int maxFruit = Integer.MIN_VALUE;
        int totalFruits = 0;
        for(int right = 0; right < fruits.length; right++){
            int fRight = fruits[right];
            map.put(fRight, map.getOrDefault(fRight, 0) + 1);
            totalFruits++;
            // Validate the widnow
            if(map.size() > 2){
                int fLeft = fruits[left];
                // Decrement left fruit from the hashmap
                map.put(fLeft, map.get(fLeft) - 1);
                // Decrement total fruits
                totalFruits--;
                
                // If the count of map happens to be zero
                if(map.get(fLeft) == 0){
                    // Pop the left key from the hashmap
                    map.remove(fLeft);
                }
                left++;
            }
            
            maxFruit = Math.max(maxFruit, totalFruits);
        }
        return maxFruit;
    }
}