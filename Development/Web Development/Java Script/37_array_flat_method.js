const arr = [
    ['zone-1', 'zone-2'],
    ['zone-3', 'zone-4'],
    ['zone-5', 'zone-6'],
    [
        'zone-7',
        [
            'zone-8',
            ['zone-9', 'zone-10']
        ]
    ]
];

console.log(arr);

// array flat() method - Used to convert n-dimension array into 1 dimensional array
console.log(arr.flat(Infinity));    // Infinity - It is used when we don't know how many no. of array are available inside a array