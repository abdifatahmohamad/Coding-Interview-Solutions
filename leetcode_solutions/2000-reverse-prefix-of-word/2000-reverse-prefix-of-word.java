class Solution {
    public String reversePrefix(String word, char ch) {
      // Convert the word string into a character array
        char[] charArray = word.toCharArray();
        
        int i = 0;
        
        // Find the index of the target character
        while (i < charArray.length && charArray[i] != ch) {
            i++;
        }
        
        // Reverse the prefix if the target character is found
        if (i < charArray.length) {
            int j = 0;
            
            // Swap characters from the start and end of the array until they meet in the middle
            while (j < i) {
                char temp = charArray[j];
                charArray[j] = charArray[i];
                charArray[i] = temp;
                
                j++;
                i--;
            }
        }
        
        // Create a new string from the modified character array
        return new String(charArray);
    }
}