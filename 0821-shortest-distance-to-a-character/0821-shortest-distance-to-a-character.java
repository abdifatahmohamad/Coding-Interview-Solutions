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
        int[] res = new int[s.length()];
        // Find the closest occurrence of c for index 0
        for (int i = 0; i < chars.length; i++) {
            res[i] = findClosestOccurrence(i, indices, count);
        }
        return res;
        
    }   
    // Helper method to find the closest occurrence of 'e' for an index
    private static int findClosestOccurrence(int index, int[] indices, int count) {
        int minDistance = Integer.MAX_VALUE;

        for (int j = 0; j < count; j++) {
            int distance = Math.abs(index - indices[j]);

            if (distance < minDistance) {
                minDistance = distance;
            }
        }

        return minDistance;
    }
}

