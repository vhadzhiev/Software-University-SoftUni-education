function solve(matrix) {
    let magicNum = 0;

    matrix[0].forEach(item => {
        magicNum += item;
    });

    // for (rowIndex = 1; rowIndex < matrix.length; rowIndex++) {
    //     let sum = 0;
    //     matrix[rowIndex].forEach(item => {
    //         sum += item;
    //     });
    //     if (sum !== magicNum) {
    //         return false;
    //     }
    // }

    let matrixSize = matrix[0].length
    for (colIndex = 0; colIndex < matrixSize; colIndex++) {
        let colSum = 0;

        for (rowIndex = 0; rowIndex < matrix.length; rowIndex++) {
            let rowSum = 0;
            colSum += matrix[colIndex][rowIndex];
            matrix[rowIndex].forEach(item => {
                rowSum += item;
            });
            if (rowSum !== magicNum) {
                return false;
            }
        }
        
        if (colSum !== magicNum) {
            return false;
        }
    }

    return true;
}

console.log(solve([
    [4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]
]));
console.log(solve([
    [11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]
]));
console.log(solve([
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
]));