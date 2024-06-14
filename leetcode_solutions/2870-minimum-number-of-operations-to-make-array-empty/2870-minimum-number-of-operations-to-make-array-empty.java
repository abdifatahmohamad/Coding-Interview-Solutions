class Solution {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (Integer n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        
        int res = 0;
        for (int freq : map.values()) {
            // If the frequency is 1, it's not possible to empty the array
            if (freq == 1) {
                return -1;
            }

            // Variable to store the number of operations needed for the current element
            int operations = 0;
            // Calculate operations based on the frequency
            if (freq % 3 == 0) {
                // If the frequency is a multiple of 3, calculate the operations directly
                operations = freq / 3;
            } else if (freq % 3 == 1) {
                // If the frequency leaves a remainder of 1 when divided by 3
                // Calculate operations as one more than the quotient of val divided by 3
                operations = (freq / 3) + 1;
            } else if (freq % 3 == 2) {
                // If the frequency leaves a remainder of 2 when divided by 3
                // Calculate operations as one more than the quotient of val divided by 3
                operations = (freq / 3) + 1;
            }

            // Update the total operations count
            res += operations;
        }

        // Return the total operations needed to empty the array
        return res;
        
    }
}