class Solution {
    public int[] productExceptSelf(int[] nums) {
       int n = nums.length;
        int[] res = new int[n];
        // Arrays.fill(res, 1);
        res[0] = 1;

        int leftProduct = 1;
        for (int i = 1; i < n; i++) {
            res[i] = nums[i - 1] * res[i - 1];
        }
        
        // for(int num : res){
        //     System.out.println(num);
        // }

        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return res;
    }
}

/*
  Test case1:
  nums = [1,2,3,4]
  for 1: 2 * 3 = 6 * 4 = 24
  for 2: 1 * 3 * 4 = 12
  for 3: 1 * 2 * 3 = 8
  for 4:  1 * 2 * 3 = 6
  
  Result = [24, 12, 8, 6]
  
  Test case2:
  nums = [-1,1,0,-3,3]
  for -1: 1 * 0 * -3 * 3 = 0
  for 1: -1 * 0 * -3 * 3 = 0
  for 0: -1 * 1 * -3 * 3 = 9
  for -3: -1 * 1 * 0 * 3 = 0
  for 3: -1 * 1 * 0 * -3 = 0
  Result = [0, 0, 9, 0, 0]
  
*/