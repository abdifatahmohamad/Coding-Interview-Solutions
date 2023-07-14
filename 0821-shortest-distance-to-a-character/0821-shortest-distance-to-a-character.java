class Solution {
    public int[] shortestToChar(String s, char c) {
        char[] chars = s.toCharArray();
        int[] indices = new int[chars.length];
        int count = 0;
        // Iterate over the char array and store the indices
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == c) {
                indices[count] = i;
                count++;
            }
        }
        
        // Initialize the result array
        int[] res = new int[s.length()];

        // Loop through the string again and find the closest occurrence of 'e' for index 0
        for (int i = 0; i < chars.length; i++) {
            int minDistance = Integer.MAX_VALUE;

            for (int j = 0; j < count; j++) {
                int distance = Math.abs(i - indices[j]);

                if (distance < minDistance) {
                    minDistance = distance;
                }
            }

            res[i] = minDistance;
        }
        
        
        return res;
        
    }
    
    // System.out.print(chars[i] + " ");
}

/*
    s = "loveleetcode"
    c = "e"
    
    Output: [3,2,1,0,1,0,0,1,2,2,1,0]


*/