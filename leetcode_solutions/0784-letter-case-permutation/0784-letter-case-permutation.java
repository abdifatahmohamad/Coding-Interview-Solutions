class Solution {
    public List<String> letterCasePermutation(String original) {
        List<String> result = new ArrayList<>(); // Initialize the result list to store transformations
        backtrack(original, "", result); // Call the backtrack method to generate transformations
        return result; // Return the final result
    }

    // Backtracking method to generate transformations recursively
    private static void backtrack(String original, String current, List<String> result) {
        if (current.length() == original.length()) {
            result.add(current); // Add the current transformation to the result list
        } else {
            char c = original.charAt(current.length()); // Get the next character from the original string
            if (Character.isLetter(c)) { // If it is a letter
                backtrack(original, current + Character.toLowerCase(c), result); // Recursively generate lowercase transformation
                backtrack(original, current + Character.toUpperCase(c), result); // Recursively generate uppercase transformation
            } else {
                backtrack(original, current + c, result); // If it is not a letter, append the original character
            }
        }
    }
}