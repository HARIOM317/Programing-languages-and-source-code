const { Script } = require("vm");

const age = 20;

age < 18 ? console.log("You can not vote!") : age == 18 ? console.log("You need voter i'd") : console.log("You can vote.");
