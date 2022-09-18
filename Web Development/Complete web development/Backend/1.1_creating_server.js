console.log("Hello world!");

// Note : Press ctrl+c to close the server in vs code

// Creating a server using nodejs
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end("Hello World!");     // print "Hello World!" on server.
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
});