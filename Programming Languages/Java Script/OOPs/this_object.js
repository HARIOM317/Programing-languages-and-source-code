// this object is that it contains the current context.

console.log(this);



// this inside function
console.log("\n\nthis inside function:");
function myName(){
    console.log(this);
}
myName();


// this inside object
console.log("\n\nthis inside object:");
const obj = {
    name: "HSR",

    myName() {
        console.log(this);
    }
}
obj.myName();


// this object does not work in arrow function
console.log("\n\nthis inside object using arrow function:");
const obj2 = {
    name: "HSR",

    myName: () => {
        console.log(this);
    }
}
obj2.myName();