const express = require("express");
const path = require("path");

const app = express();
var mongoose = require('mongoose');
const bodyparser = require('body-parser');
mongoose.connect('mongodb://localhost/contactDance', {useNewUrlParser: true});
const port = 8000;

// Define mongoose schema
var contactSchema = new mongoose.Schema({
    name: String,
    email: String,
    phone: String,
    address: String,
    age: String,
    desc: String
});

var Contact = mongoose.model('Contact', contactSchema);

// app.use(express.static('public', options));

// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static'));    // for serving static files
app.use(express.urlencoded());


// PUG SPECIFIC STUFF
app.set('view engine', 'pug')   // set the template engine 
app.set('views', path.join(__dirname, 'views'));    // set the views directory


// ENDPOINTS
app.get('/', (req, res)=>{
    const params = { };
    // serving home.pug
    res.status(200).render('home.pug', params);
});
app.get('/contact', (req, res)=>{
    const params = { };
    // serving contact.pug
    res.status(200).render('contact.pug', params);
});
// save contact form in mongodb database
app.post('/contact', (req, res)=>{
    var myData = new Contact(req.body);
    myData.save().then(()=>{
        res.send("This item has been saved to the database")
    }).catch(()=>{
        res.status(400).send("Item was not saved to the database")
    });
});


// START THE SERVER
app.listen(port, ()=>{
    console.log(`The application started successfully on port ${port}`);
});
