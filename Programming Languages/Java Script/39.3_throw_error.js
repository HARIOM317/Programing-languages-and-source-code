// throwing an error
try{
    throw new Error("I am custom error");
} catch(e) {
    console.log(e.name);
    console.log(e.message);
}

// throwing reference error
try{
    throw new ReferenceError("I am custom reference error");
} catch(e) {
    console.log(e.name);
    console.log(e.message);
}