
function rotation(array, x) {
    let m;
    let arr = [];
    let arr1 = [];

    for (let index = 0; index < array.length; index++) {
        if (array[index] === x) {
            m = index;
        }
    }

    for (let index = 0; index < array.length; index++) {
        if (index <= m) {
            arr.push(array[index])
        } else {
            arr1.push(array[index])
        }
    }
    return arr1 + "," + arr;
}

const result = rotation([1, 2, 3, 4, 5, 6], 2);

console.log(result);