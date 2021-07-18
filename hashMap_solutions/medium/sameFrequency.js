// ex. sameFrequency([1,2,3], [4,1,9]) ==> true
// ex. sameFrequency([4,4,1], [4,1,9]) ==> false (must be same frequency)

// O(n) time | O(1) space
function sameFrequency(arr1, arr2){
        if(arr1.length !== arr2.length){
        return false;
    }

    let frequencyCounter1 = {};
    let frequencyCounter2 = {};

    for(let val of arr1){
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }

    for(let val of arr2){
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1
    }

    for(let key in frequencyCounter1){
        if(!(key ** 2 in frequencyCounter2)){
            return false;
        }

        if(frequencyCounter2[key ** 2] !== frequencyCounter1 [key]){
            return false;
        }
    }

    return true;
}

console.log(sameFrequency([1, 2, 3, 2], [4, 4, 1, 9])); // true

console.log(sameFrequency([4,4,1], [4,1,9])); // false