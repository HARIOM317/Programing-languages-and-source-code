// 1: Add Dec at the end of Array
// 2: What is the return value of array?
// 3: Update march to March
// 4: Delete june from Array
// 5: Delete all items after April

// Perform these all operation using a single method (slice)

const months = ['Jan', 'march', "April", 'June', 'July'];

// solution 1
const newMonths = months.splice(months.length, 0, "Dec");   // start from array length, delete nothing, insert Dec at last index
console.log(months);


// solution 2
console.log(newMonths);     // return empty array


// solution 3
// getting index og march
const indexOfMarch = months.indexOf('march');
if(indexOfMarch != -1){
    const updateMonths = months.splice(indexOfMarch, 1, 'March')   // start from index of march, delete 1 element, insert March at index 1
} else {
    console.log("No such data found!");
}
console.log(months);


// solution 4
const indexOfJune = months.indexOf('June');
if (indexOfMarch != -1) {
    const deleteJune = months.splice(indexOfJune, 1)   // start from index of june, delete 1 element
} else {
    console.log("No such data found!");
}
console.log(months);

// solution 5
const indexOfApril = months.indexOf('April');
if (indexOfApril != -1) {
    const deleteAllItems = months.splice(indexOfApril, Infinity)   // start from index of April, delete all element
} else {
    console.log("No such data found!");
}
console.log(months);