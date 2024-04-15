const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter a number : ', (num) => {
    console.log(`Table of : ${num}\n`);

    // for loop
    for(let i = 1; i <= 10; i++){
        console.log(num + " * " + i + " = " + num*i);
    }
    rl.close();
});