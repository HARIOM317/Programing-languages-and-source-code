const { resolve } = require("path");

let p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("Promise Completed");
        resolve(1);
    }, 3000);
})

p1.then(() => {
    console.log("Handler 1");
})

p1.then(() => {
    console.log("Handler 2");
})

p1.then(() => {
    console.log("Handler 3");
})

p1.then(() => {
    console.log("Handler n");
})