// Common JS Modules

const greet = () => {
    console.log("Good Morning Everyone!");
}

const greetWithName = (user) => {
    console.log("Good Morning Dear " + user);
}

// exporting methods
module.exports = {greet, greetWithName};