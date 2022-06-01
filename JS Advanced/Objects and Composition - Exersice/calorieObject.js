function solve(arr) {
    let obj = {}

    for (let index = 0; index < arr.length; index +=2) {
        let prod = arr[index];
        let cal = arr[index + 1];
        obj[prod] = Number(cal);
    }

    console.log(obj);
}

solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);
solve(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']);