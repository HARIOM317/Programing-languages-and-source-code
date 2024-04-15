async function getWeather() {
    let delhiWeather = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("28 degree celsius");
        }, 3000);
    })
    let bhopalWeather = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("25 degree celsius");
        }, 2000);
    })
    let puneWeather = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("31 degree celsius");
        }, 7000);
    })

    console.log('Fetching delhi weather...');
    let delhiW = await delhiWeather;
    console.log("Delhi weather: ", delhiW);

    console.log('Fetching bhopal weather...');
    let bhopalW = await bhopalWeather;
    console.log("Bhopal weather: ", bhopalW);

    console.log('Fetching pune weather...');
    let puneW = await puneWeather;
    console.log("Pune weather: ", puneW);

    return [delhiW, bhopalW, puneW];
}

function greet(){
    console.log("\n\nWelcome Friends!\n\n");
}

console.log("Weather Info:");
let w = getWeather();
w.then((value) => {
    console.log(value);
});

greet();