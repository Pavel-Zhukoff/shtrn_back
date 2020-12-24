const socket = io('/');
const myPeer = new Peer(null, {
  host: peerjs_host,
  port: peerjs_port,
  debug: 3
});
const peers = {};