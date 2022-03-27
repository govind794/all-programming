// [1,2,4,2] -> [1,4,4,16]

// {1:1, 2:2, 4:1}

// {1:1, 4:2, 16:1}

function findSqure(arr1, arr2) {

    let mappedArr1 = {};
    let mappedArr2 = {};

    for (let item of arr1) {
        mappedArr1[item] = (mappedArr1[item] || 0) + 1;
    }

    for (let item2 of arr2) {
        mappedArr2[item2] = (mappedArr2[item2] || 0) + 1;
    }

    for (let key of arr1) {
        if (!mappedArr2[key * key]) {
            return false;
        }

        if (mappedArr1[key] !== mappedArr2[key * key]) {
            return false;
        }
    }
    return true;
}

const result = findSqure([1, 0, 4, 2], [1, 4, 16, 4]);
console.log(result);