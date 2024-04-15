const readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let number = Math.floor((Math.random() * 100) + 1);

let isCorrect = false;
let totalAttempt = 0;

function takeUserInput() {
    rl.question('Please Enter The Number: ', (userInput) => {
        totalAttempt++;
        if (userInput == number) {
            console.log(`Total Attempt : ${totalAttempt}`);
            console.log("You guess correct number!");
            isCorrect = true;
            rl.close();
        } else {
            if (userInput < number) {
                console.log(`\nTotal Attempt : ${totalAttempt}`);
                console.log("You guess incorrect number!");
                console.log("Your guess is too low\n");
            } else {
                console.log(`\nTotal Attempt : ${totalAttempt}`);
                console.log("You guess incorrect number!");
                console.log("Your guess is too high\n");
            }
            takeUserInput(); // Continue to prompt the user
        }
    });
}

takeUserInput(); // Start the first input prompt
