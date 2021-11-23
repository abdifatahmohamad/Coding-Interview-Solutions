function getLargestWeight(w0, w1, w2){
    let hash = new Map()
    hash.set(w0, 0);
    hash.set(w1, 1);
    hash.set(w2, 2);
  
    let largest = -99999;
    for (const key of hash.keys()) {
      if(key > largest){
        largest = key
      }
    }
    return hash.get(largest)
  }
  
  console.log(getLargestWeight(85, 100, 90))

// ---------------------------------------------
function getLargestWeight(w0, w1, w2){
    let hash = new Map()
    hash.set(w0, 0);
    hash.set(w1, 1);
    hash.set(w2, 2);
  
    let largest = -Infinity;
    for (const [key, value] of hash.entries()) {
      if(key > largest){
        largest = key
      }
    }
    return hash.get(largest)
  }
  
  w0 = 85
  w1 = 100 // return the index of this value
  w2 = 90
  console.log(getLargestWeight(w0, w1, w2))


