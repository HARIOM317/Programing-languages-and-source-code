let numbers = [12, 34, 45, 87, 97, 5, 56, 13, 87, 68];
let numbers2 = [100, 200, 300, 400, 500];

// toString()
console.log(numbers);
console.log(numbers.toString());

// join()
console.log(numbers.join('_***_'));

// pop()
console.log(numbers.pop()); // return popped element

// push()
console.log(numbers.push(100)); // return new array length

// shift()
numbers.shift(); // remove first element from array
console.log(numbers);

// unshift()
numbers.unshift(50); // add new element at the first in array
console.log(numbers);

// concat()
console.log(numbers.concat(numbers2));

// reverse()
console.log("Reverse array : ", numbers.reverse());

// sort()
console.log("Default sorted array :", numbers.sort()); // it will sort this, first come that numbers which starts from 1, then starts from 2 and so on.

// if we want to sort it in ascending or descending order then we need to pass an compare function inside sort method.
let ascendingSort = (a, b)=>{
    return a-b;
}
let descendingSort = (a, b)=>{
    return b-a;
}
console.log("Ascending Sorted Array :", numbers.sort(ascendingSort));
console.log("Descending Sorted Array :", numbers.sort(descendingSort));


// splice() - first argument: start from, second argument: how much elements you want to delete from from first argument index, last argument: new elements which you want to insert in array 
let num = [3, 4, 2, 5, 8, 9, 11];
num.splice(2, 3, 100, 200, 300, 400, 500); // starts from index 2, delete 3 elements from index 2, add new elements(100, 200, 300, 400, 500) from index 2
console.log("num after splice : ", num);

// -------------------------------------------------

// delete operator
delete numbers[2]; // it will not change the array length
console.log(numbers);