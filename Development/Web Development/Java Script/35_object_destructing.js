const myBioData = {
    firstName: "Hariom",
    lastName: "Rajput",
    age: 20,
    degree: "B.Tech",
    branch: "Computer Science"
}

let {fName, lName, age, degree, branch, address = "Ashta"} = myBioData;

console.log("My first name is", fName);
console.log("My last name is", lName);
console.log("My age is", age);
console.log("My degree is", degree);
console.log("My branch is", branch);
console.log("My address is", address);