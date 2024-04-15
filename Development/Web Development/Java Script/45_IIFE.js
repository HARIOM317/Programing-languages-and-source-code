let a = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(500);
        }, 2000);
    });
}

// IIFE - Immediately Invoked Function Expression (It is used to run async await)
(async () => {
    let b = await a();
    console.log(b);
    let c = await a();
    console.log(c);
    let d = await a();
    console.log(d);
})()
