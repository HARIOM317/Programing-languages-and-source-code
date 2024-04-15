let arr = [35, 57, 22, 97, 87, 14, 10];

// ----- ARRAY map, filter and reduce methods -----

// 1. map method - map creates a new array
console.log('\n\n---------- Map Method ----------');
let resultArr = arr.map((value) => {
    return value > 35;
})
console.log(resultArr);

arr.map((value, index) => {
    console.log(index, value);
})

arr.map((value, index, array) => {
    console.log(`Index no = ${index} and the value is ${value} belong to ${array}`);
})


// 2. filter method
console.log('\n\n---------- Filter Method ----------');
let arr2 = [4, 2, 3, 8, 12, 33, 9, 65, 23, 50];

let newArr = arr2.filter((num) => {
    return num < 10;
})
console.log("\nFiltered array : ", newArr);


// 3. reduce method
// The reduce() method executes a reducer function (that you provides) on each element of the array, resulting in a single output value.
console.log('\n\n---------- Reduce Method ----------');
let arr3 = [10, 20, 30, 40, 50];

let reducedArr = arr3.reduce((num1, num2) => {
    return num1 + num2; // sum of all elements of array
})
console.log(reducedArr);