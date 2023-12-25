class Animal{
    constructor(name){
        this._name = name;
    }

    // getter
    get name(){
        return this._name;
    }

    // setter
    set name(newName){
        this._name = newName;
    }

    walk(){
        console.log(`${this.name} is walking.`);
    }
}

class Dog extends Animal{
    bark(){
        console.log("Dog is barking");
    }
}

a = new Animal("Monkey");
a.walk();
a.name = "Sankey Monkey"
console.log(a.name);

d = new Dog("Puppy");
d.bark();
d.walk();


let b = "HSR";
// instanceof operator
console.log(a instanceof Animal);
console.log(b instanceof Animal);
console.log(d instanceof Animal);