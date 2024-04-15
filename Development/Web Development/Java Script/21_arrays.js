let fruits = ['Mango', 'Banana', 'Guava', 'Orange', 'Apple', 'Pineapple', 'Grape', 'Lichee'];

fruits[2] = 'Watermelon';
fruits[fruits.length] = 'Guava';
fruits.pop();
fruits.push('Papaya')

console.log(fruits);

for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}