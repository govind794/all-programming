// hello -> llloh

// {h:1, e:1, l:2, o:1}

// {l:3, a:1, o:1, h:1}

function isAnagram(s1, s2) {
    if (s1.length !== s2.length) {
        return false;
    }

    let count = {};
    for (let letter of s1) {
        count[letter] = (count[letter] || 0) + 1
    }

    for (let item of s2) {
        if (!count[item]) {
            return false;
        }

        count[item] -= 1;
    }
    return true;
}

const result = isAnagram('govind', 'dniovg');

console.log(result);