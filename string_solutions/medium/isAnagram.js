// Return true if anagram and false if not
// ex. 'elbow' === 'below' => true
// ex. 'Dormitory' === dirty room##'

function isAnagram(str1, str2){
    return stringFormat(str1) === stringFormat(str2);
}

// Create helper function:
function stringFormat(str){
    return str
        .replace(/[^\w]/g, '')
        .toLowerCase()
        .split('')
        .sort()
        .join('');
}

str1 = 'dirty room';
str2 = 'Dormitory';
console.log(isAnagram(str1, str2));