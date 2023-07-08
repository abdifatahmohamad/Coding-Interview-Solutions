class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
         int rows = image.length;
        int cols = image[0].length;

        for (int i = 0; i < rows; i++) {
            reverseRow(image[i]); // Reverse the current row

            // Flip and invert each element in the row
            for (int j = 0; j < cols; j++) {
                image[i][j] = 1 - image[i][j]; // Flip and invert the current element
            }
        }

        return image;
    }

    private void reverseRow(int[] row) {
        int start = 0;
        int end = row.length - 1;
        while (start < end) {
            int temp = row[start];
            row[start] = row[end];
            row[end] = temp;
            start++;
            end--;
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