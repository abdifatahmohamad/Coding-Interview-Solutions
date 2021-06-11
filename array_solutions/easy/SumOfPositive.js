
// You get an array of numbers, return the sum of all of the positives ones.
// Example [1,-4,7,12] => 1 + 7 + 12 = 20

// SOLUTION 1 Using for... of loop:
function positiveSum(arr) {
    let sum = 0;
    for(let num of arr){
        if(num >= 0){
            sum += num;
        }
    }
    return sum;
  
}

arr = [1,-4,7,12]
console.log(positiveSum(arr))


// SOLUTION 2 Using high order function (reduce())
arr = [1, -4, 7, 12]
const positiveSum = arr.reduce((sum, curr) => curr > 0 ? sum + curr : sum, 0);
console.log(positiveSum);