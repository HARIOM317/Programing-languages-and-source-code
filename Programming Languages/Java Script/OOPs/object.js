let bioData = {
    myName: "Hariom Singh Rajput",
    myAge: 20,
    degree: "B.Tech",
    branch: "CSE",

    getData: function(){
        console.log(`Name: ${this.myName}`);
        console.log(`Age: ${this.myAge}`);
        console.log(`Degree: ${this.degree}`);
        console.log(`Branch: ${this.branch}`);
    }
}

bioData.getData();