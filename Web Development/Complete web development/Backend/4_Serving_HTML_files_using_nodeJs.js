const http = require('http');
// importing fs module
const fs = require('fs');
// serving html file
const fileContent = fs.readFileSync('36_transform_in_css.html');

// creating a server
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-type': 'text/html' });
    res.end(fileContent);
});

// listen on 80 port
server.listen(80, '127.0.0.1', () => {
    console.log("Listening on port 80");
});
