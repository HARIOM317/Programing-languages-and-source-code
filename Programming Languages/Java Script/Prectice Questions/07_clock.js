let count = 0;
let time = setInterval(() => {
    let date = new Date();
    let h = date.getHours();
    let m = date.getMinutes();
    let s = date.getSeconds();

    console.clear();
    console.log(`Time : ${h}:${m}:${s}`);
    count++;

    if(count == 30){
        clearInterval(time);
    }
}, 1000);
