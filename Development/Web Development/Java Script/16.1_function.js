//  function to find a factorial
function factorial (n){
    let fact = 1;
    for(let i = 2; i <= n; i++){
        fact *= i;
    }
    return fact;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter a number for Factorial : ', (num) => {
    let ans = factorial(num);

    console.log(`Factorial of ${num} is ${ans}`);

    rl.close();
});