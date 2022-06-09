function sort(arr, str) {
    let result = [];

    if (str == 'asc') {
        result = arr.sort((a, b) => a - b);
    } else {
        result = arr.sort((a, b) => b - a);
    }
    return result;
}

console.log(sort([14, 7, 17, 6, 8], 'asc'));
console.log(sort([14, 7, 17, 6, 8], 'desc'));