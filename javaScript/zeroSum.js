// This method use in only short array
// checing sume zero

// [-5,-4,-3,-2,0,2,4,6,8]
// [-4,4]

// function isSumeZero(array) {
//     for (let no of array) {
//         for (let i = 1; i < array.length; i++) {
//             if (no + array[i] === 0) {
//                 return [no, array[i]];
//             }
//         }
//     }
// }

// const result = isSumeZero([-5,-4,-3,-2,0,2,4,6,8]);


function getSumOfZeroPair(array) {
    let left = 0;
    let right = array.length - 1

    while (left < right) {
        let sum = array[left] + array[right];
        if (sum === 0) {
            return [array[left], array[right]];
        } else if (sum > 0) {
            right--;
        } else {
            left++;
        }
    }
}

const result = getSumOfZeroPair([-5, -4, -3, -2, 0, 2, 6, 8]);

console.log(result);