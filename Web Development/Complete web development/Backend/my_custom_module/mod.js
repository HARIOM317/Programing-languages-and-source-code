// creating average function
/*
function average(arr) {
    let sum = 0;
    arr.forEach(element => {
        sum += element;
    });
    return sum / arr.length;
}

// make it function
module.exports = average;
*/


// creating sum function
function addition(arr) {
    let sum = 0;
    arr.forEach(element => {
        sum += element;
    });
    return sum;
}

// make it object
module.exports = {
    add: addition,
    name: "Hariom",
    repo: "GitHub"
};

// Note: This is also a object
module.exports.collage = "SISTec";