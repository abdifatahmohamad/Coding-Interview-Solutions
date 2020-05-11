/* Use higher order functions such as map(), filter(), reduce(), 
forEach(), every(), some(), sort() and so on to solve a complex problems. */

/* Using map() method, create a function that takes an array with numbers 
 and return an array with the elements multiplied by two..*/

const getMultipliedArr = (arr) => arr.map((num) => num * 2);

console.log(getMultipliedArr([1, 2, 4, 6]));
// Output: [ 2, 4, 8, 12 ]
