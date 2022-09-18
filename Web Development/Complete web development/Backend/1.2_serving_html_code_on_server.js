console.log("Hello world!");

// Creating a server using nodejs
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;

    // serving html code
    res.setHeader('Content-Type', 'text/html');

    // write html code inside this
    res.end(`
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transition in CSS</title>
</head>

<style>
    #box1 {
        display: flex;
        margin: 20px;
        width: 200px;
        height: 200px;
        background-color: cornflowerblue;

        justify-content: center;
        align-items: center;
        color: white;

        transition: background-color 2s ease-in 0.5s;
    }

    #box1:hover {
        background-color: black;
        color: aqua;
        width: 250px;
        height: 250px;
        border: 2px solid lightgreen;
        border-radius: 150px;
        font-size: 30px;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }


    #box2 {
        display: flex;
        margin: 20px;
        width: 200px;
        height: 200px;
        background-color: cornflowerblue;

        justify-content: center;
        align-items: center;
        color: white;

        transition: all 2s ease-in 0.5s;
    }

    #box2:hover {
        background-color: black;
        color: aqua;
        width: 250px;
        height: 250px;
        border: 2px solid lightgreen;
        border-radius: 150px;
        font-size: 30px;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
</style>

<body>
    <h3>This is CSS Transition</h3>
    <div class="container">
        <div id="box1">
            This is my box1
        </div>
        <div id="box2">
            This is my box2
        </div>
    </div>
</body>

</html>`)
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
});