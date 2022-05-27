function addRemove(arr) {
    let number = 1;
    const result = [];

    for (let command of arr) {
        if (command == 'add') {
            result.push(number);
        } else {
            result.pop();
        }
        number++;
    }

    if (result.length != 0) {
        for (let element of result) {
            console.log(element);
        }
    } else {
        console.log('Empty')
    }
}