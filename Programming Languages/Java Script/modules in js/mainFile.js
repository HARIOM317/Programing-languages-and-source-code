// Without Destructuring
// const hello = require("./module1");
// hello.greet();
// hello.greetWithName("Hariom");

// Using Destructuring
const { greet, greetWithName } = require("./module1");  // Common js modules

// import sum from "./module2.js";   // ES6 Modules (It will work when type = module in package.json)

greet();
greetWithName("Hariom Singh Rajput");

// let addition = sum(10, 20);
// console.log("Sum = ", addition);
// myIntro("Hariom Singh Rajput", "Software Engineer");
