class Vehicle{
    constructor(color, name){
        this.color = color;
        this.name = name;
    }

    showDetail(){
        console.log("Name: ", this.name);
        console.log("Color: ", this.color);
    }
}

class Car extends Vehicle{
    constructor(price, speed){
        super();
        this.price = price;
        this.speed = speed;
    }
    carSpeed(){
        console.log(`Max speed is ${this.speed} KM/H`);
    }
    carPrice(){
        console.log("Price: ", this.price);
    }
}

let c1 = new Car("20000000 INR", 320);
c1.color = "Red";
c1.name = "Farari";
c1.showDetail();
c1.carSpeed();
c1.carPrice();
