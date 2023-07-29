class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0, right = 0;
        int maxFruit = Integer.MIN_VALUE;
        while(right < fruits.length){
            int fRight = fruits[right];
            map.put(fRight, map.getOrDefault(fRight, 0) + 1);
            if(map.size() > 2){
                int fLeft = fruits[left];
                if(map.get(fLeft) == 1){
                    map.remove(fLeft);
                }else{
                    map.put(fLeft, map.get(fLeft) - 1);
                }
                left++;
            }
            maxFruit = Math.max(maxFruit, right - left + 1);
            right++;
        }
        return maxFruit;
    }
}