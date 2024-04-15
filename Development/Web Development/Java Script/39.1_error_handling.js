// Note: We can handle only synchronous process using try-catch (It will not work with asynchronous process or scheduled program)

// Solution: We need to use try-catch inside asynchronous program (not asynchronous program into try-catch), i.e.

// asynchronous program
setTimeout(() => {
    try{
        console.log(a+b);
    } catch(error) {
        console.log("Error: Babu a and b are not defined!")
    }
}, 3000);


// synchronous program
try{
    let a = 10;
    let b = 0;

    let c = a/b;
    console.log(c);

    console.log(Done);  // Error: Done is not defined
} catch(error){
    console.log("Error occurred!");
}

console.log("Hey, I am Done!");
console.log("Feeling Happy 😊😊");