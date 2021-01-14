const express = require('express');
const app = express();
const ExpressPeerServer = require('peer').ExpressPeerServer;
const https = require('https');
const cors = require('cors');
const fs = require('fs');

const sslOptions = {
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
};

const server = https.createServer(sslOptions, app).listen(443);

// CORS
app.use(cors());

app.use('/', ExpressPeerServer(server, {debug:true}));
