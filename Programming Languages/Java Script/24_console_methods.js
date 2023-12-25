// clear - to clear the console
console.clear();

// log
console.log("\nConsole log is used to print something on console!\n");

// error
console.error("Console error is used to show something in form of error!\n")

// warn
console.warn("Console warn is used to show something in form of warning!\n")

// info
console.info("Console info is used to show something in form of information!\n")

// table - to show object in table form
obj = {a:1, b:2, c:3, d:4, e:5};
console.table(obj);


console.time("forLoop");

for(let i = 0; i < 100000; i++){
    if(i==100000){
        console.log(">>> For loop ends");
    }
}

console.timeEnd("forLoop"); // it prints the total time taken to execute the for loop