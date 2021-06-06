function palindrome(str){
    // reverse string
        let revString = '';

        for(let char of str){
            revString = char + revString;
        }

    return revString === str;
}

// Another way to solve is to use two pointers:
const palindrome = str =>{
    let left = 0;
    let right = str.length-1;

    while(left < right){
        if(str[left] !== str[right]){
            return false;
        }
        left += 1;
        right -= 1;
    }
    return true;
}

let str = "level";
console.log(palindrome(str));