// finally - code of finally block will always execute even error occur or not

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// asynchronous process
rl.question('Please enter your age: ', (userInput) => {
    try {
        if (userInput >= 1 && userInput <= 120) {
            console.log(`You are ${userInput} years old`);
        } else {
            rl.close();
            throw new Error("Error: You Entered Invalid Age!");
        }

        rl.close();
    } catch (error) {
        console.log("Error Name :", error.name);
        console.log("Error Message :", error.message);
    } finally {
        console.log("\nHey, I will always execute!");
        console.log("🤓🤓🤓");
    }
});
