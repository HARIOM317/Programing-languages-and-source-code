// Problem - Multiply each element by 2 and return those elements which is greater that 10?

let arr = [2, 3, 4, 5, 6, 7, 8];

let arr2 = arr.map((element) => {
    return element*2;
}).filter((element) => {
    return element > 10;
});

console.log(arr2);