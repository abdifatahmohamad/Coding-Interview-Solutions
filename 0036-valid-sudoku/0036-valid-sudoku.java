class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        Set<String> seen = new HashSet<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char ch = board[r][c];
                if (ch != '.') {
                    String rowVal = "r" + r + ch;
                    String colVal = "c" + c + ch;
                    String blockVal = "b" + (r / 3) + (c / 3) + ch;
                    
                    if (seen.contains(rowVal) || 
                        seen.contains(colVal) || 
                        seen.contains(blockVal)) {
                        return false;
                    }

                    seen.add(rowVal);
                    seen.add(colVal);
                    seen.add(blockVal);
                }
            }
        }

        return true; 
    }
}