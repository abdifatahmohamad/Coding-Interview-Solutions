function reverseInt(int){
    let revInt = '';
    for(let num of int.toString()){
        revInt = num + revInt;
    }

    return parseInt(revInt) * Math.sign(int);
    
    // An easy solution
    // const revInt = int.toString().split('').reverse().join('');
    // return parseInt(revInt) * Math.sign(int);
}

int = -123;
console.log(reverseInt(int));