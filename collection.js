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

/*Write a function sort that takes an array filled with 3 numbers and returns these 3 numbers sorted 
in ascending order as an array. sort([2, 3, 1]) should return [1, 2, 3].*/

function sort(arr){
  let numbers = [2,1,3 ];
  return numbers.sort();
}

console.log(sort()); //should return [1, 2, 3].

/*Problem: Transform this simple sorting algorithm into a unique sort,
meaning it should not return any duplicate value in the 
sorted array */

const uniqSort = function(arr){
  let cache = {};
  const result = [];

  for(let i = 0; i < arr.length; i++){
    let array = arr[i]
    if(!cache[array]){
      result.push(array);
      cache[array] = true;
    }
  }
  return result.sort((a,b) => a-b);
}

console.log(uniqSort([4,2,2,3,2,2,2]));

//Output => [2,3,4]

/* Write a function which takes in a string and returns
counts of each character in the string */

function charCount(str) {
	let result = {};
	for (let el of str) {
		let char = el.toLowerCase();
		if (/[a-z0-9]/.test(char)) {
			//Meaning is already in there
			if (result[char] > 0) {
				result[char]++;
			} else {
				//Meaning is not in there yet
				result[char] = 1;
			}
		}
	}
	return result;
}

console.log(charCount('hhhrr!!! &&  !'));

/* A palindrome is a word, sentence or other type of character sequence 
which reads the same backward as forward. For example, “racecar” and “Anna” are palindromes. 
“Table” and “John” aren’t palindromes, because they don’t read the same from left to right 
and from right to left. */

function isPalindrome(str){
    str = str.toLowerCase();
    return str === str.split('').reverse().join('');
}

console.log(isPalindrome('racecar'));
// palindrome('racecar')  ===  true
// palindrome('table')  ===  false

// Merge sorted arrays 
function mergeSortedArrays(arr1, arr2){
//let combine = arr1.concat(arr2);
 let combine = [...arr1, ...arr2];
 return combine.sort((a,b) => a - b);
}

mergeSortedArrays([0,3,4,31], [3,4,6,30]);



