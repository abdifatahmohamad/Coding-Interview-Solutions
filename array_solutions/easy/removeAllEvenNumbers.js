// O(N) Time and Space
function removeAllEvenNumbers(arr){
    let odds =[]
    for (let num of arr){
        if(num % 2 != 0){
            odds.push(num)
        }
    }
    return odds;
}



let arr = [1,2,4,5,10,6,3];
// Output: [1,5,3]
console.log(removeAllEvenNumbers(arr));