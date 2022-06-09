function fibonacci() {
    let x = 0;
    let y = 1;

    function calc() {
        let result = x + y;
        x = y;
        y = result;
        return x;
    }

    return calc;
}

let fib = fibonacci();
console.log(fib()); 
console.log(fib()); 
console.log(fib()); 
console.log(fib()); 
console.log(fib()); 
console.log(fib()); 
console.log(fib());
