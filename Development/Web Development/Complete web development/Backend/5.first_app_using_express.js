// importing express
const express = require("express");

// creating express app
const app = express();
const port = 80;


//  >>>>> GET REQUEST METHOD <<<<<
// Home section
// app.get("/", (req, res) => {
//     res.send("This is homepage of my first express app");
// });

// sending status code
app.get("/", (req, res) => {
    res.status(200).send("These are our services on express app");
});

// About section
app.get("/about", (req, res) => {
    res.send("This is about section of my first express app");
});
// Services section
app.get("/services", (req, res) => {
    res.send("These are our services on express app");
});

// custom template
app.get("/this", (req, res) => {
    res.status(404).send("This page is not found!");
});



//  >>>>> POST REQUEST METHOD <<<<<
app.post("/about", (req, res) => {
    res.send("This is the post request for about");
});
app.post("/services", (req, res) => {
    res.send("This is the post request for services");
});


// listening
app.listen(port, () => {
    console.log(`The application started successfully on port ${port}`);
});