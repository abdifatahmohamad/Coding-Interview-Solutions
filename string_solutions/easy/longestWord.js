// One way to solve this problem is to use a regular for loop (best solution)
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

// Another way to solve is to use Array.prototype.sort():
function findLongestWord(str){
    let strSplit = str.split(' ');

    const longestWord = strSplit.sort((a, b) =>{
    return b.length - a.length;
});

    return longestWord[0];
}

// The third way to solve is to use Array.prototype.sort():
function findLongestWord(str){
    let strSplit = str.split(' ');

    const longestWord = strSplit.reduce((curr_word, longest) =>{
    if(curr_word.length >  longest.length){
        return curr_word;
    } else{
        return longest
    }
});

    return longestWord;
}

let str = "Abdifatah Abdiweli Mohamed";
console.log(longestWord(str));
