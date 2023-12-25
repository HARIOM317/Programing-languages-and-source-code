// Strings are immutable.
let str = "Hariom";
console.log(`String : ${str}`);
console.log(`Length : ${str.length}`);

str[3] = 'a'; // it will not change because strings are immutable
console.log(str);