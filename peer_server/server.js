const express = require('express');
const app = express();
const ExpressPeerServer = require('peer').ExpressPeerServer;
const https = require('https');
const fs = require('fs');

const sslOptions = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

const server = https.createServer(sslOptions, app).listen(443);

// CORS
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use('/', ExpressPeerServer(server, {debug:true}));