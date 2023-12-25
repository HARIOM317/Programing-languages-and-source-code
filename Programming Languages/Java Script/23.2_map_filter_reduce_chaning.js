// Problem - Multiply each element by 2 and return sum of those elements which is greater that 10?

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let ans = arr.map((element) => element * 2).filter((element) => element > 10).reduce((num1, num2) => {
    return num1 + num2;
})

console.log(ans);