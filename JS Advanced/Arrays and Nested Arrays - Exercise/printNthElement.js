function printNthElement(array, step) {
    return array.filter((element, index) => index % step == 0);
}