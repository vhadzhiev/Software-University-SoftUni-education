function calculator() {
    let num1;
    let num2;
    let result;

    function init(n1, n2, r) {
        num1 = document.querySelector(n1);
        num2 = document.querySelector(n2);
        result = document.querySelector(r);
    }

    function add() {
        result.value = Number(num1.value) + Number(num2.value);
    }

    function subtract() {
        result.value = Number(num1.value) - Number(num2.value);
    }

    return {
        init,
        add,
        subtract
    }
}