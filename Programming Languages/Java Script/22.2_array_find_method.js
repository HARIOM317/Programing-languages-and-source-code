let array = [-10, -20, -30, 40, 50, 60, 70, -80, 90, -100];

// find method
let found = array.find((element) => {
    // return first element which is greater then 0
    return element > 0;
})

console.log(found);