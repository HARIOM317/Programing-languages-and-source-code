function mainFunction(callback){
    console.log("Performing Operation...");

    setTimeout(() => {
        console.log("Operation Completed!");
    }, 2000);
}

// callback function
function callbackFunction(result){
    console.log("Processing...");
    console.log("Result : ", result);
}

// Calling the main function with the callback function
mainFunction(callbackFunction);
setTimeout(() => {
    console.log("\n\n");
    mainFunction(callbackFunction("Good!"));
}, 3000);