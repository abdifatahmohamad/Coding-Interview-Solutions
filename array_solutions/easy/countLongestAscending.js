function countLongestAscending(nums){
    let longestAscending = 1, currentLongestLength = 1;

    // Loop through the nums from the 2nd element
    for(let i=1; i<nums.length; i++){
        // Check if the current element is greater than previous element
        if(nums[i] > nums[i-1]){
            currentLongestLength++
        } else{
            if(longestAscending < currentLongestLength){
                longestAscending = currentLongestLength;
            }

            currentLongestLength = 1;
        }
    }

    if(longestAscending < currentLongestLength){
        longestAscending = currentLongestLength;
    }

    return longestAscending;
}

console.log(countLongestAscending([-1, 3, 5, 2, 5, 3, 9, 4, 8, 10, 12, 6])); // Output: 4
console.log(countLongestAscending([5, 6, 3, 5, 7, 8, 9, 1, 2])); // Output: 5

// nums = [-1, 3, 5, 2, 5, 3, 9, 4, 8, 10, 12, 6]
// longest ascending 4 8 10 12 
// answer = 4 