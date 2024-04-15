// function currying

function sum(num1){
    return function(num2){
        return function(num3){
            console.log(`Sum of ${num1}, ${num2} and ${num3} is ${num1+num2+num3}`);
        }
    }
}

sum(5)(3)(8);
