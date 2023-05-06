// importing average function from mod.js
// use average function
/*
const average = require("./mod");
console.log(average);
console.log("Average = ", average([3, 4, 5]));
console.log("This is index.js");
*/

// use object
const mod = require("./mod");
console.log(mod.add([3, 4, 5, 98, 10, 12]));
console.log(mod.name);
console.log(mod.repo);
console.log(mod.collage);

