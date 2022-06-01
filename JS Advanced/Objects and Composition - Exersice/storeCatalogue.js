function solve(arr) {
    let obj = {};

    for (const line of arr.sort()) {
        let [product, price] = line.split(' : ');
        let letter = product[0];
        if (!obj[letter]) {
            obj[letter] = {};
        }
        obj[letter][product] = price;
    }

    for (const letter of Object.keys(obj)) {
        console.log(letter)
        let sortedProducts = Object.keys(obj[letter])
        
        for (const product of sortedProducts) {
            console.log(`  ${product}: ${obj[letter][product]}`)
        }
    }
}

solve(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
]);
solve(['Banana : 2',
    'Rubic\'s Cube: 5 ',
    'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10'
]);