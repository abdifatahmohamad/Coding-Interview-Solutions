// ex. 'aabbccddeee' count the occurrence of characters

//SOLUTION 1-  using for...of loop
function count(str){
    // Turn string into an array
    const arr = Array.from(str);
    let seen = {};
    for(let char of arr){
      console.log(char);
        if (char in seen){
            seen[char] ++;
        } else{
            seen[char] = 1
        }
    }
    return seen
}

let str = 'aabbccddeee';
console.log(count(str));

// SOLUTION 2- using the Array.prototype.reduce 
const count = Array.from('aabbccddeee').reduce((acc, char) => {
    if (char in acc) {
      acc[char]++;
    } else {
      acc[char] = 1;
    }
    return acc;
  }, {});

  console.log(count(str));