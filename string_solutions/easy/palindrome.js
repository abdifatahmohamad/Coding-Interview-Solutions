function palindrome(str){
    // reverse string
        let revString = '';

        for(let char of str){
            revString = char + revString;
        }

    return revString === str;
}

let str = "level";
console.log(palindrome(str));