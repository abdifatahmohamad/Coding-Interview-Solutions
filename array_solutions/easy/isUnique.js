// O(N) time | O(N) space
function isUnique(str){
    let hashSet = {};
    let strToReturn = '';
    for(let char of str){
        if(!(char in hashSet)){
            strToReturn += char;
            hashSet[char] = 1;
        }
    }
    return strToReturn;
}

let str = "aabc";
console.log(isUnique(str));