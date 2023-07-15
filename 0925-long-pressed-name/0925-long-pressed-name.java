class Solution {
    public boolean isLongPressedName(String name, String typed) {
        // Case1: handle if name length > typed length 
        if (name.length() > typed.length()) {
            return false;
        }
        int i = 0, j = 0;
        // Keeping looping until we have processed all characters in either name or typed
        while (i < name.length() || j < typed.length()) {
            // Check if we are within the bounds of both name and typed,
            // and if the characters at the current positions i and j match
            if (i < name.length() && j < typed.length() && name.charAt(i) == typed.charAt(j)) {
                i++;
                j++;
                // handle the case where the current character in typed is a repeated character.
            } else if (j > 0 && j < typed.length() && typed.charAt(j) == typed.charAt(j - 1)) {
                // Skip repeated characters in typed
                j++; 
            } else {
                // Mismatched characters
                return false; 
            }
        }
        
        return true;
    }
}

/*
    - Order is matter
    - typed length always >= name length
    - All characters in typed is in name
    
    Case1: If name length > typed length : return false
    Case2: If string name != string typed: return false
    Case3: if first character of typed != first character of typed: return false
    
    Test cases:

    1. name = "alex", typed = "aaleex" : return true
    2. name = "saeed", typed = "ssaaedd" : return false
    3. name = "rick", typed = "kric": return false
    4. name = "xnhtq", typed = "xhhttqq": return false
    5. name = "alex", typed = "aaleexa": return false

*/