const { error } = require("console");

// promises are the solution of the callback hell

// promise 1
let promise1 = new Promise(function (resolve, reject) {
    console.log("I am Happy 😊");
    resolve("HSR");
})

// promise 2
let promise2 = new Promise((resolve, reject) => {
    console.log("\nPromise is Pending..");
    setTimeout(() => {
        console.log("\n\nPromise completed successfully!");

        // resolving the promise
        resolve(true);
    }, 3000);
})

// promise 3
let promise3 = new Promise((resolve, reject) => {
    console.log("\nPromise is Pending..");
    setTimeout(() => {
        console.log("\n\nPromise rejected!");

        // throwing an error and rejecting the promise
        reject(new Error("Something went wrong!"));
    }, 5000);
})

console.log(promise1);
console.log(promise2);
console.log(promise3);


promise1.then((value) => {
    console.log("Promise1 value is: ", value);
})

// handling promise error on reject
promise3.catch((error) => {
    console.log("Error Handled!");
})