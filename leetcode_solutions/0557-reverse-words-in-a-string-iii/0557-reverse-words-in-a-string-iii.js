/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.split(" ");
    let res = []
    for(let i=0; i<s.length; i++){
        let word = swap(s[i])
        res.push(word);
     }
     return res.join(' ');

};

function swap(word){
  // let w = Array.from(word);
  // This also works
  let w = [...word];
  let l = 0;
  let r = w.length - 1;
  while (l < r){
    let temp = w[l];
    w[l] = w[r]
    w[r] = temp
    l += 1
    r -= 1
  }
  return w.join('')
};