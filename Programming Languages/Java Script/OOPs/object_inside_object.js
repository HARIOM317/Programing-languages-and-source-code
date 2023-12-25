let bioData = {
    myName: {
        firstName: "Hariom",
        middleName: "Singh",
        lastName: "Rajput"
    },
    myAge: 20,
    degree: "B.Tech",
    branch: "CSE",

    getData: function () {
        console.log(`Name: ${this.myName.firstName} ${this.myName.lastName}`);
        console.log(`Age: ${this.myAge}`);
        console.log(`Degree: ${this.degree}`);
        console.log(`Branch: ${this.branch}`);
    }
}

bioData.getData();