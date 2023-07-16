class Solution {
    public boolean checkIfExist(int[] arr) {
        int i = 0; 
        int j = 1; 
         // Continue while j pointer is within array bounds
        while (j < arr.length) {
            if (arr[i] == 2 * arr[j] || arr[j] == 2 * arr[i]) {
                // If either arr[i] is equal to 2 times arr[j] or arr[j] is equal to 2 times arr[i]
                return true; // Found a match, return true
            }

            // If j pointer is at the end of the array
            if (j == arr.length - 1) {
                i++; 
                j = i + 1; // Set j pointer to the element next to i pointer
            } else {
                // If j pointer is not at the end of the array
                j++; 
            }
        }

        return false;   
    }
}

/*
  arr = [10,2,5,3]
  i != j
  0 <= i, j < arr.length
  arr[i] == 2 * arr[j]
  
  For i = 0 and j = 2, 
  arr[i] == 10 == 2 * 5 == 2 * arr[j]

*/