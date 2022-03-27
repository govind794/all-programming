// count a uniqe number

// [1,1,2,2,3,3,4,4,5,5,6,7,8,9]

// function uniqeNo(array) {
//     let uniqe = {};

//     for (let num of array) {
//         uniqe[num] = (uniqe[num] || 0) + 1
//     }

//     for (let key of array) {
//         if (uniqe[key] == 1) {
//             console.log(key);
//         }
//     }
// }

// uniqeNo([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]);


function isUniqeNo(array) {
    if (array.length) {
        let i = 0;
        for (let j = 1; j < array.length; j++) {
            if (array[i] !== array[j]) {
                i++;
                array[i] = array[j];
            }
        }
        console.log(array);
        return i + 1;
    } else {
        throw new Error("Array should not be empty");
    }
}

const result = isUniqeNo([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]);

console.log(result);