function fruit(fruit, weightInGrams, pricePerKg) {
    let weightInKgs = weightInGrams / 1000;
    let totalPrice = weightInKgs * pricePerKg;

    console.log(`I need $${totalPrice.toFixed(2)} to buy ${weightInKgs.toFixed(2)} kilograms ${fruit}.`);
}

fruit('orange', 2500, 1.80);
fruit('apple', 1563, 2.35);