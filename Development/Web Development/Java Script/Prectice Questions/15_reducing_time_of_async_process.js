let p1 = async () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(20);
        }, 4000);
    })
}

let p2 = async () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(30);
        }, 2000);
    })
}

let p3 = async () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(50);
        }, 3000);
    })
}

const result = async () => {
    console.time("run");

    // more time : 4 + 2 + 3 = almost 9 seconds
    // let a1 = await p1();
    // let a2 = await p2();
    // let a3 = await p3();

    // less time: max process time (almost 4 seconds)
    let a1 = p1();
    let a2 = p2();
    let a3 = p3();

    let completeWork = await Promise.all([a1, a2, a3]);
    console.log(completeWork);

    console.timeEnd("run");
}

result();