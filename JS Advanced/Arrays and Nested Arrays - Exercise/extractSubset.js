function extract(arr) {
    let biggest = Number.NEGATIVE_INFINITY
    let newArr = []

    for (num of arr) {
        if (num >= biggest) {
            biggest = num;
            newArr.push(num);
        }
    }

    return newArr;
}

extract([1,
    3,
    8,
    4,
    10,
    12,
    3,
    2,
    24
]);
extract([1,
    2,
    3,
    4
]);
extract([20,
    3,
    2,
    15,
    6,
    1
]);