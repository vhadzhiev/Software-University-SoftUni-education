function cooking(number, ...operations) {
    let result = Number(number);

    let chop = (x) => x / 2;
    let dice = (x) => Math.sqrt(x);
    let spice = (x) => x + 1;
    let bake = (x) => x * 3;
    let fillet = (x) => x * 0.8;

    for (let i = 0; i < operations.length; i++) {
        switch (operations[i]) {
            case "chop":
                result = chop(result);
                console.log(result);
                break;
            case "dice":
                result = dice(result);
                console.log(result);
                break;
            case "spice":
                result = spice(result);
                console.log(result);
                break;
            case "bake":
                result = bake(result);
                console.log(result);
                break;
            case "fillet":
                result = fillet(result);
                console.log(result);
                break;
        }
    }
}

cooking("32", "chop", "chop", "chop", "chop", "chop");
cooking("9", "dice", "spice", "chop", "bake", "fillet");