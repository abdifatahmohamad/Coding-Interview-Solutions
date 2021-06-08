// Remove from the array whatever is in the following arguments.
// Return the leftover values in an array:
// ex. seekAndDestroy([2,3,4,6,6, 'hello'], 2,6) ==> [3,4, 'hello']

// Solution 1 using arguments, indexOf, filter
function seekAndDestroy(arr){
    // Turn the whole arguments into an array:
    const args = Array.from(arguments);

    // Create a helper function that checks target numbers
    // and returns true if NOT in the actual array:
    function filterArr(arr){
        // Return true if NOT in the array:
        return args.indexOf(arr) === -1;
    }

    // filter() return only if something is true
    // Pass filterArr() into filter method(high order function method)
    return arr.filter(filterArr);
}

// Solution 2 using ...rest, filter & includes
function seekAndDestroy(arr, ...rest){
    return arr.filter(val => !rest.includes(val));
}

console.log(seekAndDestroy([2,3,4,6,6, 'hello'], 2,6));



