function longestWord(str){
    let strSplit = str.split(' ');
    let longestWord = 0;
    let curr_word = null;

    for(let i=0; i<strSplit.length; i++){
        if(strSplit[i].length > longestWord){
            longestWord = strSplit[i].length;
            curr_word = strSplit[i];
        }
    }

    return curr_word;
}

let str = "Abdifatah Abdiweli Mohamed";
console.log(longestWord(str));
