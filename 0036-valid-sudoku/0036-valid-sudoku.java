class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                if (value != '.') {
                    // Check and create a new set if needed for rows
                    if (!rows.containsKey(r))
                        rows.put(r, new HashSet<>());
                    // Check and create a new set if needed for columns
                    if (!cols.containsKey(c))
                        cols.put(c, new HashSet<>());
                    // Check and create a new set if needed for squares
                    int squareIndex = 3 * (r / 3) + c / 3;
                    if (!squares.containsKey(squareIndex))
                        squares.put(squareIndex, new HashSet<>());

                    // Check if the value is already present in rows, columns, or squares
                    if (rows.get(r).contains(value) || 
                        cols.get(c).contains(value) ||
                        squares.get(squareIndex).contains(value))
                        return false;

                    // Add the value to the respective row, column, and square
                    rows.get(r).add(value);
                    cols.get(c).add(value);
                    squares.get(squareIndex).add(value);
                }
            }
        }

        return true;
    }
}