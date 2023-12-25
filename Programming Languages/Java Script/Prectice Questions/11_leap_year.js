const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please Enter a Year: ', (year) => {
    // logic for leap year
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                console.log(`${year} is a leap year.`);
            } else {
                console.log(`${year} is not a leap year.`);
            }
        } else {
            console.log(`${year} is a leap year.`);
        }
    } else {
        console.log(`${year} is not a leap year.`);
    }

    rl.close();
});