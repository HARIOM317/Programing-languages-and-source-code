const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter your favorite color: ', (userInput) => {
    switch (userInput) {
        case 'red':
            console.log("Your favorite color is red!");
            break;
        case 'green':
            console.log("Your favorite color is green!");
            break;
        case 'blue':
            console.log("Your favorite color is blue!");
            break;
        default:
            console.log(`Your favorite color is other, which is: ${userInput}`);
    }
    rl.close();
});