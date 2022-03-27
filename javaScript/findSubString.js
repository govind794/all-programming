// str -> govind
// sub str -> vi

function subString(str, substr) {
    let num = 0;
    for (let index = 0; index < str.length; index++) {
        if (str[index] === substr[num]) {
            num += 1
        }
    }
    if (num === substr.length) {
        console.log("Sub string match successfully");
    } else {
        console.log("does not match sub string");
    }
}

const result = subString("govind", "govind");
// console.log(result);