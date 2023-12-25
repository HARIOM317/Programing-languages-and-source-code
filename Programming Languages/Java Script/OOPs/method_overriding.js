class Employee{
    login(){
        console.log("Base (login): Logged in as an employee");
    }
    logout(){
        console.log("Base (logout): Logged out from the application");
    }
    requestLeaves(){
        console.log("Base (requestLeaves): Requested for leaves");
    }
    promotion(){
        console.log("Base (promotion): Promotion requested");
    }
}

class Programmer extends Employee {
  salary(amount) {
    console.log(`Derived (salary): Programmer's Salary is ${amount}`);
  }

  // method overriding
  promotion() {
    super.promotion();  // calling super class promotion() method
    console.log("Derived (promotion): Awarded a certification");
  }

  // method overriding
  requestLeaves() {
    console.log(
      "Derived (requestLeaves): Employee is not allowed to make leave requests"
    );
  }
}

let p1 = new Programmer();
p1.login();
p1.promotion();
p1.requestLeaves();
p1.salary("$ 50000");
p1.logout();