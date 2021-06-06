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

// The third way to solve is to use Array.prototype.reduce():
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

// Fourth way to solve is to use sort() + filter():
function longestWord(str){
    // Put away alphanumeric value
    const wordArr = str.toLowerCase().match(/[a-z0-9]+/g);


    // Sort the array by length:
    const sorted = wordArr.sort((a, b) =>b.length - a.length);
    

    // If there is multiple words, put them into an array:
    const longestWordArr = sorted.filter(word => word.length === sorted[0].length);

    // Check if more than one array value:
    if(longestWordArr.length === 1){
        return longestWordArr[0];
    } else{
        return longestWordArr;
    }
}

let str = "Hello, there my name Abdifatah Mohamed!";
console.log(longestWord(str));
