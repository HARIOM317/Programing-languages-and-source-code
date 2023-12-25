let p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 1");
    }, 1000);
});

let p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        reject(new Error("Error"));
    }, 2000);
});

let p3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 3");
    }, 3000);
});

// do something when all the promises have completed even any of them has rejected
let promise_all = Promise.allSettled([p1, p2, p3]);

promise_all.then((value) => {
    console.log(value);
});