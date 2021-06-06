function chunkArray(arr, len){
    // Initialize an empty array
    const chunkedArr = [];

    // Loop through the array
    for(let val of arr){
        // Get the last element
        const last = chunkedArr[chunkedArr.length - 1];
        // const last = chunkedArr.slice(-1)[0];

        // Check if the last and if last.length === chunk length
        if(!last || last.length === len){
            chunkedArr.push([val]);
        }else{
            last.push(val);
        }
    }

    return chunkedArr;
}

console.log(chunkArray([1, 2, 3, 4, 5, 6, 7], 3));