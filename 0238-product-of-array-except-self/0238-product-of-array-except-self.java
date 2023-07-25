class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = product;
            product *= nums[i];
        }
        
        for(int n : res){
            System.out.print(n + " "); // 1 1 2 6 
            // [4, 3, 2, 1]
            //  1 1 2 6
            // [24, ]
        }

        product = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= product;
            product *= nums[i];
            //nums = 4, 3, 2, 1
            // res = 1, 1, 2, 6
            // product = 1
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