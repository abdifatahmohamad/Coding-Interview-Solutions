/* Use higher order functions such as map(), filter(), reduce(), 
forEach(), every(), some(), sort() and so on to solve a complex problems. */

/* Using map() method, create a function that takes an array with numbers 
 and return an array with the elements multiplied by two..*/

const getMultipliedArr = (arr) => arr.map((num) => num * 2);

console.log(getMultipliedArr([1, 2, 4, 6]));
// Output: [ 2, 4, 8, 12 ]

// Find ages above 21 using FILTER method
const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];
const canDrink = ages.filter(age => age >= 21);

console.log(canDrink);

// Get all the companies that started in 80s using FILTER method
const companies= [
  {name: "Company One", category: "Finance", start: 1981, end: 2004},
  {name: "Company Two", category: "Retail", start: 1992, end: 2008},
  {name: "Company Three", category: "Auto", start: 1999, end: 2007},
  {name: "Company Four", category: "Retail", start: 1989, end: 2010},
  {name: "Company Five", category: "Technology", start: 2009, end: 2014},
  {name: "Company Six", category: "Finance", start: 1987, end: 2010},
  {name: "Company Seven", category: "Auto", start: 1986, end: 1996},
  {name: "Company Eight", category: "Technology", start: 2011, end: 2016},
  {name: "Company Nine", category: "Retail", start: 1981, end: 1989}
];
const eightiesCompanies = companies.filter(company => company.start >= 1980 && company.start < 1990);
console.log(eightiesCompanies);

