function removeDuplicates(arr){
    // let seen = new Set();
    let hashSet = {};
    let arrayToReturn = [];
    for(let num of arr){
        if(!(num in hashSet)){
            arrayToReturn.push(num);
            // hashSet[num] = true;
            hashSet[num] = 1;
        }
    }

    return arrayToReturn;
}

let arr = [1, 2, 1, 4, 6, 8, 3, 9, 5, 3, 6, 8, 5, 9]
console.log(removeDuplicates(arr)); // [1, 2, 4, 6, 8, 3, 9, 5]
