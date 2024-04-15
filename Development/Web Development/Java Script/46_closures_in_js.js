function init() {
    var name = "Mozilla Fire Fox";

    // displayName() is the inner function, a closure
    function displayName(){
        console.log("Name:", name);
    }

    return displayName;
}

let c = init();
c();