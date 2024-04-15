// Synchronous Programming
let a = prompt("What is your name?");
let b = prompt("What is your age?");
let c = prompt("What is your address?");

console.log(`${a} is ${b} years old and lives in ${c}`);

// Asynchronous Programming
console.log("Asynchronous Programming")
setTimeout(() => {
    console.log("Hey, How are you?");
}, 3000);

console.log("I am Good!");
