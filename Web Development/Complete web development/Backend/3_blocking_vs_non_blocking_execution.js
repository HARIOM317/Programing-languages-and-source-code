// Synchronous(blocking) code : line by line execution
// Asynchronous(non-blocking) code : callback will fire and line by line execution is not guaranteed.

// Note: NodeJs works on non-blocking I/O modal and this modal based on callbacks.

// Asynchronous (non-blocking) behavior
const fs = require("fs");
fs.readFile("61.2_new_file.txt", "utf-8", (err, data) => {
    // first argument of function is error and second is data
    // If no error will found then it returns null in place of error.
    console.log(data);
});
console.log("This is a message!");
console.log("This is the example of non-blocking code.");