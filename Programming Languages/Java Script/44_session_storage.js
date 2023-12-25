// The session storage exists only within the current browser tab

let key = "name";
let value = "HSR";

sessionStorage.setItem(key, value);

console.log(sessionStorage.getItem(key));

sessionStorage.removeItem(key);

sessionStorage.clear();     // remove all data