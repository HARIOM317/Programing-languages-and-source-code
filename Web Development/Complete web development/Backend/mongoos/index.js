var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/test', { useNewUrlParser: true, useUnifiedTopology: true });

// Connecting mongodb to nodejs
var db = mongoose.connection;
// error exception
db.on('error', console.error.bind(console, 'connection error:'));

// db.once('open', function () {
//     console.log("We are connected");
// });

// creating a schema that name can be only a string.
var kittySchema = new mongoose.Schema({
    name: String
});

// use method
kittySchema.methods.speak = function () {
    var greeting  = "My name is "+ this.name
        // ternary operator
        // ? "My name is " + this.name
        // : "I don't have a name";
    console.log(greeting);

}

// locking the schema
var kitten = mongoose.model('hsrKitty', kittySchema);

var hsrKitty = new kitten({ name: 'hsrKitty' });
var hsrKitty2 = new kitten({ name: 'hsrKitty2' });
// console.log(hsrKitty.name);
// hsrKitty.speak();


// save
// create collection of name hsrKitties (automatically ad s in last of name)
hsrKitty.save(function (err, hsrKitty){
    if (err) return console.error(err);
    // hsrKitty.speak();
});
hsrKitty2.save(function (err, k){
    if (err) return console.error(err);
    // k.speak();
});

kitten.find({name: "hsrKitty2"}, function(err, kittens){
    if (err) return console.error(err);
    console.log(kittens);
});