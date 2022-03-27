
// [1,2,3,4,5,6,7,8,9,10]

// find index no of 5 
// 4
// time complexity -> linear O(n)

// function findIndexNo(array, n) {
//     if (!array.length) {
//         throw new Error('Array length not be empty');
//     } else {
//         for (let index = 0; index < array.length; index++) {
//             if (array[index] == n) {
//                 return index;
//             }
//         }
//     }
// }

// divide and conquer technique
// time complexity -> binary O(log(n))
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
// middle element -> 8
// divide array
// [1, 2, 3, 4, 5, 6, 7]

function findIndexNo(array, n) {
    let min = 0;
    let max = array.length - 1;

    while (min <= max) {
        let middleIndex = Math.floor((min + max) / 2);
        if (array[middleIndex] < n) {
            min = middleIndex + 1;
        } else if (array[middleIndex] > n) {
            max = middleIndex - 1;
        } else {
            return middleIndex;
        }
    }
    return -1;
}

const result = findIndexNo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1);
console.log(result);

