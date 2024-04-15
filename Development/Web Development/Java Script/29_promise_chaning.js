const { resolve } = require("path");

// promise
let p1 = new Promise((resolve, reject) => {
    console.log("\nPromise is Pending..");
    setTimeout(() => {
        console.log("\n\nPromise completed successfully!");

        // resolving the promise
        resolve(true);
    }, 3000);
})

p1.then((value) => {
    console.log("P1 : ", value);

    // promise 2
    let p2 = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Promise 2");
        }, 2000);
    })

    return p2;
}).then((value) => {
    console.log("We are almost done!");

    // Automatically converted in a promise with value 12
    return 12;  // returning constant value
}).then((value) => {
    console.log("We are completely done!");
})