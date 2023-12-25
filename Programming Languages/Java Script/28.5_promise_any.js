let p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 1");
    }, 3000);
});

let p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        reject(new Error("Error"));
    }, 2000);
});

let p3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 3");
    }, 4000);
});

// Promise.any() - return those promise which completed or resolve firstly even any of them has rejected
let promise_all = Promise.any([p1, p2, p3]);

promise_all.then((value) => {
    console.log(value);
});