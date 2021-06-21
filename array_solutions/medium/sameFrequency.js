// ex. sameFrequency([1,2,3], [4,1,9]) ==> true
// ex. sameFrequency([4,4,1], [4,1,9]) ==> false (must be same frequency)

// SOLUTION 1- Naive approach - O(n^2) time | O(1) space
// function sameFrequency(arr1, arr2){
//     if(arr1.length !== arr2.length){
//         return false;
//     }

//     for(let i=0; i<arr1.length; i++){
//         // find the square of 1st index in arr1 that is in arr2
//         let correctIndex = arr2.indexOf(arr1[i] ** 2);
//         if(correctIndex === -1){
//             return false;
//         } else{
//             // Splice removes 1 index from arr2
//             arr2.splice(correctIndex, 1);
//         }
//     }

//     return true;
// }

// SOLUTION 1- Naive approach
function sameFrequency(arr1, arr2){
        if(arr1.length !== arr2.length){
        return false;
    }

    let frequencyCounter1 = {};
    let frequencyCounter2 = {};

    for(let val of arr1){
        /*if(val in frequencyCounter1){
            frequencyCounter1[val] ++;
        } else{
            frequencyCounter1[val] = 1;
        }*/

        // Same way as the above code:
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }

    for(let val of arr2){
        /*if(val in frequencyCounter2){
            frequencyCounter2[val] ++;
        } else{
            frequencyCounter2[val] = 1;
        }*/

        // Same way as the above code:
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1
    }

    for(let key in frequencyCounter1){
        if(!(key ** 2 in frequencyCounter2)){
            return false;
        }

        if(frequencyCounter2[key ** 2] !== frequencyCounter1[key]){
            return false;
        }
    }

    // console.log(frequencyCounter1);
    // console.log(frequencyCounter2);

    return true;
}

console.log(sameFrequency([1, 2, 3, 2], [4, 4, 1, 9])); // true

console.log(sameFrequency([4,4,1], [4,1,9])); // false