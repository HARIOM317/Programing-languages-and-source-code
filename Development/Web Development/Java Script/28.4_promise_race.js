let p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 1");
    }, 3000);
});

let p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 2");
    }, 2000);
});

let p3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Value 3");
    }, 4000);
});

// Promise.race() - return those promise which completed or resolve firstly
let promise_all = Promise.race([p1, p2, p3]);

promise_all.then((value) => {
    console.log(value);
});