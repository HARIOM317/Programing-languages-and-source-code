// There are 7 types of primitives data types in java script (Null, Numbers, String, Symbol, Undefined, Boolean, BigInt)

let a = null;
let b = 80;
let c = true;
let d = BigInt("76768687") + BigInt("10000000");
let e = "Hariom";
let f = undefined;
let g = Symbol("I am a nice symbol");
let h;

console.log(a, typeof(a));
console.log(b, typeof(b));
console.log(c, typeof(c));
console.log(d, typeof(d));
console.log(e, typeof(e));
console.log(f, typeof(f));
console.log(g, typeof(g));
console.log(h, typeof(h));

// There is a non-primitives data type available in java script called object

const myInfo = {
    "name": "Hariom",
    "lastNmae": "Rajput",
    "age": 20,
    "phone": 9302765839,
    "isPlaced": false
}

console.log(myInfo['name']);
console.log(myInfo['phone']);
console.log(typeof myInfo);