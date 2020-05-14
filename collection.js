/* Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
*/

let fizzBuzz = function (n) {
	let numbers = [];
	for (let i = 1; i <= n; i++) {
		if (i % 3 === 0 && i % 5 === 0) {
			numbers.push('FizzBuzz');
		} else if (i % 5 === 0) {
			numbers.push('Buzz');
		} else if (i % 3 === 0) {
			numbers.push('Fizz');
		} else {
			numbers.push(i.toString());
		}
	}
	return numbers;
};

/*Write a function getLastElement that takes an array and returns the last element of the array. 
getLastElement([1, 2]) should return 2. */

function getLastElement(arr){
   for(let i = 0;  i < arr.length; i++){
   return arr[arr.length-1];
  }
}

 console.log( getLastElement([1,2])); //should return 2


