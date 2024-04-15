// class
class Student{
    enroll(name){
        this.name = name;
        console.log("\n");
    }

    play(){
        console.log("Playing...", this.name);
    }

    study(){
        console.log("Studying...", this.name);
    }

    sing(){
        console.log("Singing...", this.name);
    }
}

// objects
let hariom = new Student();
let aman = new Student();

hariom.enroll('Hariom');
hariom.play();
hariom.sing();
hariom.study();

aman.enroll('Aman');
aman.play();
aman.sing();
aman.study();