const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();
const port = 80;

// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static'));   // for serving static files
app.use(express.urlencoded())

// PUG SPECIFIC STUFF
app.set('view engine', 'pug');   // set the template engine as pug
app.set('views', path.join(__dirname, 'views'))   // set the views directory

// ENDPOINTS
app.get("/", (req, res) => {
    const con = "Get this gym membership discount immediately by taking our yearly subscription. Offer closes soon."
    const params = { 'title': 'Row html in pug', 'content': con }
    res.status(200).render('index.pug', params);
});

app.post('/', (req, res)=>{
    // linking data
    my_name = req.body.my_name
    email = req.body.email
    date = req.body.date
    number = req.body.number
    Ac_number = req.body.Ac_number

    // writing user data
    let outputToWrite = `The name of the client is: ${my_name} \nThe email of the client is: ${email} \nThe DOB of the client is: ${date} \nThe number of the client is: ${number} \nThe Account number of the client is: ${Ac_number}`;

    // save user data in text file
    fs.writeFileSync('output.txt', outputToWrite);

    console.log(req.body);
    const params = {'message':"Your form has been submitted successfully"};
    res.status(200).render('index.pug', params);
});


// START THE SERVER
app.listen(port, () => {
    console.log(`The application started successfully on port ${port}`);
});