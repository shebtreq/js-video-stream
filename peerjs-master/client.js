var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/examples/videochat/index.html');
});

app.get('/style.css', function (req, res) {
    res.sendFile(__dirname + '/examples/videochat/style.css');
});

app.get('/peer.js', function (req, res) {
    res.sendFile(__dirname + '/dist/peer.js');
});

app.listen(3000);