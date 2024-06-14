class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int rows = image.length;
        int cols = image[0].length;

        // Invert the values in-place without flipping
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < (cols + 1) / 2; j++) {
                // Invert and flip the elements simultaneously using XOR with 1
                int temp = image[i][j] ^ 1;
                image[i][j] = image[i][cols - j - 1] ^ 1;
                image[i][cols - j - 1] = temp;
            }
        }

        return image;
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