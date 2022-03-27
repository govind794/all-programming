
// [1,2,3,4,5,6,7,8,9] 
// 4

// function largestSum(array, num) {
//     if (num > array.length) {
//         throw new Error('Array should not be empty');
//     } else {
//         let maxsum = 0;
//         for (let i = 0; i < array.length - num + 1; i++) {
//             let temp = 0;
//             for (let j = 0; j < num; j++) {
//                 temp += array[i + j];
//             }
//             if (temp > maxsum) {
//                 maxsum = temp;
//             }
//         }

//         return maxsum;
//     }
// }

function largestSum(array, num) {
    let maxsum = 0;
    let temp = 0;

    if (array.length < num) {
        throw new Error('array length should be greate then num');
    } else {
        for (let i = 0; i < num; i++) {
            maxsum += array[i];
        }
        temp = maxsum;
        for (let j = num; j < array.length; j++) {
            temp = temp - array[j - num] + array[j];
            maxsum = Math.max(maxsum, temp);
        }
        return maxsum;
    }
}

console.log(largestSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 4));