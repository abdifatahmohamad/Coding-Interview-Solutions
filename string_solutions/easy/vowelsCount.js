// SOLUTION 1 

// function vowelsCount(str){
//     let count = 0;
//     let vowels = ['a', 'e', 'i', 'u', 'o'];
//     for(let letter of str.toLowerCase()){
//         if(vowels.includes(letter)){
//             count++;
//         }
//     }
//     return `The number of vowels are: ${count} vowels`;
// }

// SOLUTION 2
function vowelsCount(str){
    let vowelsCount = 0;
    const arr = str.split('');
    for(let char in arr){
        // console.log(arr[char]);
        if(arr[char].includes("aeiou")){
            vowelsCount++;
        }
    }
    return vowelsCount;
}

console.log(vowelsCount("Abdifatah Mohamed"));