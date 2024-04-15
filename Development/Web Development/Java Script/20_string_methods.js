let str1 = "Hariom";
let str2 = "RAJPUT";
let temp = '            SUPER MAN           ';

// length (length is a Property of String)
console.log("Length of str1: ", str1.length);

// toUpperCase()/toLowerCase() - It's a method
console.log(str1.toUpperCase());
console.log(str2.toLowerCase());

// slice()
console.log(str1.slice(3,6));
console.log(str1.slice(3));

// replace()
console.log(str2.replace('PUT', 'DUT'));

// concat()
console.log(str1.concat(" ", str2));

// trim()
console.log(temp);
console.log(temp.trim());

// includes()
console.log(str1.includes('om'));

// startsWith()
console.log(str1.startsWith('H'));

// endsWith()
console.log(str1.endsWith('om'));