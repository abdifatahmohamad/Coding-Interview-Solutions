class Solution {
    public boolean isValidSudoku(char[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        Map<Integer, Set<Character>> rowsMap = new HashMap<>();
        Map<Integer, Set<Character>> colsMap = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char value = board[r][c];
                if (value != '.') {
                    // Check and create a new set if needed for rows
                    if (!rowsMap.containsKey(r))
                        rowsMap.put(r, new HashSet<>());
                    // Check and create a new set if needed for columns
                    if (!colsMap.containsKey(c))
                        colsMap.put(c, new HashSet<>());
                    // Check and create a new set if needed for squares
                    int squareIndex = 3 * (r / 3) + c / 3;
                    if (!squares.containsKey(squareIndex))
                        squares.put(squareIndex, new HashSet<>());

                    // Check if the value is already present in rows, columns, or squares
                    if (rowsMap.get(r).contains(value) || 
                        colsMap.get(c).contains(value) ||
                        squares.get(squareIndex).contains(value))
                        return false;

                    // Add the value to the respective row, column, and square
                    rowsMap.get(r).add(value);
                    colsMap.get(c).add(value);
                    squares.get(squareIndex).add(value);
                }
            }
        }

        return true;
    }
}