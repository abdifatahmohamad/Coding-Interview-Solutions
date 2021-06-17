// Given two strings s and t, return true if s is a subsequence of t, 
// or false otherwise.

// Input: s = "abc", t = "ahbgdc"
// Output: true

// Input: s = "axc", t = "ahbgdc"
// Output: false


// SOLUTION using two different pointers
function isSubsequence(s, t){
    if (s.length === 0){
        return true;
    }

    let pointer1 = pointer2 = 0;
    while(pointer1 < s.length && pointer2 < t.length){
        while(t.charAt(pointer2) !== s.charAt(pointer1)){
            pointer2++;
            if(pointer2 === t.length){
                return false;
            }
        }
        pointer1++;
        pointer2++;
    }
    return pointer1 === s.length;
}
let s = "abc";
let t = "ahbgdc";
console.log(isSubsequence(s, t));
console.log(isSubsequence("axc", "ahbgdc"));