console.log("Set Interval and Set Time out");
let timeCount = 0;

// execute after 3 seconds
setTimeout(() => {
    console.log("Set time out time exited...");
}, 3000);

// continuously run on every one second
let interval = setInterval(() => {
    console.log("Timer : ", timeCount);
    timeCount++;

    // clear the interval
    if (timeCount == 10) {
        clearInterval(interval);
    }
}, 1000);


