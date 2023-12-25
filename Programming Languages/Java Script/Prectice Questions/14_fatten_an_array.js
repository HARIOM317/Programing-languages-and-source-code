// Fatten Array - (fatten an array means to convert the 3d or 3d array into a single dimensional array)

// 2D Array
const arr = [
    ['zone-1', 'zone-2'],
    ['zone-3', 'zone-4'],
    ['zone-5', 'zone-6'],
    ['zone-7', 'zone-8'],
    ['zone-9', 'zone-10']
]
console.log(arr);

let flatArr = arr.reduce((accumulator, currentValue) => {
    return accumulator.concat(currentValue);
});

console.log(flatArr);