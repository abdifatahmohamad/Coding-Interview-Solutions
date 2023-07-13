class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0; // Pointer for the name string
        int j = 0; // Pointer for the typed string

        while (j < typed.length()) {
            if (i < name.length() && name.charAt(i) == typed.charAt(j)) {
                // Characters match, move both pointers
                i++;
                j++;
            } else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) {
                // Long-pressed character, move the pointer in the typed string
                j++;
            } else {
                // Mismatch
                return false;
            }
        }

        return i == name.length();
    }
}