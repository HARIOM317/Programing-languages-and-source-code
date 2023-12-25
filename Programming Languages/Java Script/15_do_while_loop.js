const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter a number for sum of n natural numbers : ', (num) => {
    let sum = 0;
    let i = 1;

    // do-while loop
    do{
        sum += i;
        i++;
    } while(i <= num);

    console.log("Sum of first", num, "natural number is :", sum);

    rl.close();
});