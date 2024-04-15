// class
class Student {
  // constructor
  constructor(name) {
    this.name = name;
    console.log("Enrolled", this.name);
  }

  play() {
    console.log("Playing...", this.name);
  }

  study() {
    console.log("Studying...", this.name);
  }

  sing() {
    console.log("Singing...", this.name);
  }
}

// objects
let hariom = new Student("Hariom");
let aman = new Student("Aman");

hariom.play();
hariom.sing();
hariom.study();

aman.play();
aman.sing();
aman.study();
