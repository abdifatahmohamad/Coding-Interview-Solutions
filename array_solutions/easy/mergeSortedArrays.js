

function mergeSortedArrays(arr1, arr2){
    let mergedArr = [];
    let arr1Item = arr1[0];
    let arr2Item = arr2[0];
    let i = 1, j = 1;

    // Check the input:
    if(arr1.length === 0){
        return arr2;
    }

    if(arr2.length === 0){
        return arr1;
    }

    while(arr1Item || arr2Item){
        if(!arr2Item || arr1Item < arr2Item){
            mergedArr.push(arr1Item);
            arr1Item = arr1[i];
            i++;
            } else {
                mergedArr.push(arr2Item);
                arr2Item = arr2[j]
                j++;
            }
        }    
    return mergedArr;
}

console.log(mergeSortedArrays([0, 3, 4, 31], [1, 2, 4, 6, 8, 9, 30]));