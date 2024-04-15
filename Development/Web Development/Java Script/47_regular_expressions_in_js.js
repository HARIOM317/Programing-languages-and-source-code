const regex = /very/g   // g means global (replace very globally)

const text = "I am very smart and I am very cool because my pen is very awesome that is very very beautiful";

console.log(text.replace("very", "VERY"));  // it will replace only first very -> VERY
console.log(text.replace(regex, "VERY"));  // it will replace all very -> VERY