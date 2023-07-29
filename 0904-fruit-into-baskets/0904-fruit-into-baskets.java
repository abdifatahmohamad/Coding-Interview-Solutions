class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0, right = 0;
        int maxFruit = Integer.MIN_VALUE;
        while(right < fruits.length){
            int fRight = fruits[right];
            map.put(fRight, map.getOrDefault(fRight, 0) + 1);
            // Validate if window is valid
            if(map.size() > 2){
                int fLeft = fruits[left];
                if(map.get(fLeft) == 1){
                    // remove the left fruit from the map
                    map.remove(fLeft);
                }else{
                    // Decrement the left fruit
                    map.put(fLeft, map.get(fLeft) - 1);
                }
                // Incerement our left pointer
                left++;
            }   
            // Maximize the todal number of fruits you can pick
            maxFruit = Math.max(maxFruit, right - left + 1);
            // Incerement our right pointer
            right++;
        }
        return maxFruit;
    }
}