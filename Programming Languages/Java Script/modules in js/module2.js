// ES6 Modules
const sum = (a, b) => {
    return a+b;
}

export const myIntro = (myName, myPosition) => {
    console.log(`My name is ${myName} and I am a ${myPosition}`);
}

export default sum;