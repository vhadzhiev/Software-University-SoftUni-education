function solve(arr) {
    let result = [];

    class Town {
        constructor(town, latitude, longitute) {
            this.Town = town;
            this.Latitude = Number(latitude);
            this.Longitude = Number(longitute);
        }
    }

    for (let index = 1; index < arr.length; index++) {
        let myArr = arr[index].split('|').map(t => t.trim()).filter(x => x.length != 0);
        let townName = myArr[0];
        let latitude = Number(myArr[1]).toFixed(2);
        let longitute = Number(myArr[2]).toFixed(2);
        let town = new Town(townName, latitude, longitute);
        result.push(town);
    }

    return JSON.stringify(result);
}

solve(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |'
]);
solve(['| Town | Latitude | Longitude |',
    '| Veliko Turnovo | 43.0757 | 25.6172 |',
    '| Monatevideo | 34.50 | 56.11 |'
]);