class Animal{
    constructor(name){
        this.name = Animal.capitalize(name);
    }

    walk(){
        console.log(`Animal ${this.name} is Walking`);
    }

    // static method
    static capitalize(name){
        return name.charAt(0).toUpperCase() + name.substr(1, name.length).toUpperCase();
    }
}

let animal1 = new Animal("tiger");
animal1.walk();

// static methods can access anywhere without creating object by using class name
console.log(Animal.capitalize("Tiger is very dangerous animal in jungle"));