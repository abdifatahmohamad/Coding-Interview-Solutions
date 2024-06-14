class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<>();
        for(int i = 0; i < nums.length - 2; i++){
            int l = i + 1, r = nums.length -1;
            while(l < r){
                int threeSum = nums[i] + nums[l] + nums[r];
                if(threeSum == 0){
                    set.add(List.of(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                }else if(threeSum < 0){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return new ArrayList<>(set);
    }
}