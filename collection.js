/*Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
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

// Write a function that validates the password:
function isValidPassword(password, username) {
	let tooShort = password.length < 8;
	let hasSpace = password.indexOf(' ') !== -1;
	let tooSimilar = password.indexOf(username) !== -1;
	if (tooShort || hasSpace || tooSimilar) return false;
	return true;
}
