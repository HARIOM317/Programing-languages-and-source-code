// importing express
const express = require("express");
// importing path module
const path = require("path");

// creating express app
const app = express();
const port = 80;


// for serving static files
app.use('/static', express.static('static'));
// set the template engine as pug
app.set('view engine', 'pug');
// set the views directory
app.set('views', path.join(__dirname, 'views'))
// creating pug endpoint
app.get("/demo", (req, res) => {
    res.render('demo', { title: 'hey there', message: 'Hello everyone! I am HSR' })
});


// listening
app.listen(port, () => {
    console.log(`The application started successfully on port ${port}`);
});