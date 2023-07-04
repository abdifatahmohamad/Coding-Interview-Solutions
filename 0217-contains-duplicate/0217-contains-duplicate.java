class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        boolean found = false;
        for(Integer n : nums){
            if(hashSet.contains(n)){
                found = true;
            }
            
            hashSet.add(n);
        }
        
        return found;
        
    }
}