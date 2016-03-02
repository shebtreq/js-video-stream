var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/videochat/index-cam.html');
});

app.get('/style.css', function (req, res) {
    res.sendFile(__dirname + '/videochat/style.css');
});

app.get('/peer.js', function (req, res) {
    res.sendFile(__dirname + '/node_modules/peerjs/dist/peer.js');
});

app.listen(3000);