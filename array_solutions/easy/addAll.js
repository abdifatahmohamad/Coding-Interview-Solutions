// Return a sum of all parameters entered regardless 
// of the amount of numbers --> NO ARRAYS
// ex. addAll(2,5,6,7) === 20

// Solution 1 - using old way and for loop
function addAll(){
    // Old way to turn something into an array:
    // var args = Array.prototype.slice.call(arguments);

    // A for loop to sum up those numbers:
    // var total =0;
    // for(var i=0; i<args.length; i++){
    //     total += args[i];
    // }
    // return total;


    // In ES6 way, sumUp numbers using reduce
    // const args = Array.from(arguments);
    // const sumUp = args.reduce((a, b) => a + b, 0);
    // return sumUp;

    // In ES6 way, sumUp numbers using forEach
    // const args = Array.from(arguments);
    // let sum = 0;
    // args.forEach(num => sum += num);
    // return sum;
}


// Solution 2 -- using ES6 way ...rest & forEach
function sum(...rest){
    let total = 0;
    rest.forEach(num => total += num);
    return total;
}

// Solution 2 -- using ES6 way ...rest & forEach
function sumUp(...numbers){
    return numbers.reduce((acc, curr) => acc + curr, 0);
}


console.log(addAll(4,1,8,9, 3)); // 25
console.log(sum(8,3,1,2, 4)); // 18
console.log(sumUp(7,1,5,8,2)); // 23