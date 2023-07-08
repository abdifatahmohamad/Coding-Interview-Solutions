class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
         int rows = image.length;
        int cols = image[0].length;

        for (int i = 0; i < rows; i++) {
            flipAndInvertRow(image[i]); // Flip and invert the current row
        }

        return image;
    }

    private void flipAndInvertRow(int[] row) {
        int left = 0;
        int right = row.length - 1;

        while (left <= right) {
            // Flip and invert the elements using XOR
            int temp = row[left] ^ 1;
            row[left] = row[right] ^ 1;
            row[right] = temp;

            // Move the pointers inward
            left++;
            right--;
        }
    }
        
}

/**
image = [

        [1,1,0],
        [1,0,1],
        [0,0,0]
            
        ]

Output: [

        [1,0,0],
        [0,1,0],
        [1,1,1]
        
        ]
        
        1 0 0 
        0 1 0 
        0 0 0 

*/