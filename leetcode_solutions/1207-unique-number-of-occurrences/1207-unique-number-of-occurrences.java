class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : arr){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        Set<Integer> valuesSet = new HashSet<>();
        
        for(int n : map.values()){
            if(valuesSet.contains(n)){
                return false;
            }
            
            valuesSet.add(n);
        }
        
        return true;
        
    }
}