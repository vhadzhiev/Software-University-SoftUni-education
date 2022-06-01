function register(arr) {
    let result = [];

    for (const item of arr) {
        let obj = {}
        let info = item.split(' / ');
        let name = info[0];
        let level = Number(info[1]);
        let items = info[2] ? info[2].split(', ') : [];

        obj = {name, level, items}

        result.push(obj);
    }

    console.log(JSON.stringify(result));
}

register(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
]);

register(['Jake / 1000 / Gauss, HolidayGrenade']);