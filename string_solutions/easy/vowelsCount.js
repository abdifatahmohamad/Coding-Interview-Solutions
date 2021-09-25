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
    str = str.toLowerCase();
    let count = 0;
    const arr = str.split('');
    for(let char in arr){
        if("aeiou".includes(arr[char])){
            count++;
        }
    }
    return `The number of vowels are: ${count} vowels`;
}

console.log(vowelsCount("Abdifatah Mohamed"));

// In Python:
// Solution using Python code
// def vowelsCount(s: str) -> int:
//     count = 0
//     vowels = ['a', 'e', 'i', 'u', 'o']
//     # vowels = "aeiou"
//     # lst = list(s)
//     for char in s:
//         if char in vowels:
//             count += 1
//     return count

// print(vowelsCount("abdifatah Mohamed"));