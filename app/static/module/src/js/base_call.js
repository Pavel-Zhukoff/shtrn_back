const myVideo = document.createElement('div');
myVideo.style = 'border: 2px solid red';
myVideo.append(document.createElement('video'));
const STATE = {};
navigator.getUserMedia = navigator.getUserMedia
    || navigator.webkitGetUserMedia
    || navigator.mozGetUserMedia;
const userMedia = navigator.mediaDevices.getUserMedia({
  audio: true,
  video: true,
});

const videoGrid = document.getElementById('video-grid');
socket.on('user-state-update', state => {
  Object.assign(STATE, {...state});
  console.log(STATE);
  userMedia.then(stream => {
    stream.getAudioTracks().forEach(track => {
      track.enabled = STATE.audio;
    });
    stream.getVideoTracks().forEach(track => {
      track.enabled = STATE.video;
    });
  });
});

userMedia.then(stream => {

  addVideoStream(myVideo, stream);

  myPeer.on('call', call => {
    call.answer(stream);
    let parent = document.createElement('div');
    parent.className = "watcher-item";
    let video = document.createElement('video');
    parent.appendChild(video);
    call.on('stream', userVideoStream => {
      parent.id = call.peer;
      addVideoStream(parent, userVideoStream);
    });
  });

  socket.on('user-connected', userId => {
    connectToNewUser(userId, stream);
  });
});

myPeer.on('open', id => {
  socket.emit('join-room', room_id, id, user);
  myVideo.id = id;
});

socket.on('user-disconnected', userId => {
  if (peers[userId]) peers[userId].close();
  document.getElementById(userId).remove();
});

function connectToNewUser(userId, stream) {
  const call = myPeer.call(userId, stream);
  let parent = document.createElement('div');
  parent.className = "watcher-item";
  let video = document.createElement('video');
  parent.appendChild(video);
  call.on('stream', userVideoStream => {
    parent.id = call.peer;
    addVideoStream(parent, userVideoStream);
  });
  call.on('close', () => {
    video.remove();
  });

  peers[userId] = call;
}
// Добавляет видео в сетку
function addVideoStream(el, stream) {
  let video = el.getElementsByTagName('video')[0];
  video.srcObject = stream;
  video.addEventListener('loadedmetadata', () => {
    video.play();
  });
  videoGrid.append(el);
}

function toggleLogic(a, b) {
  return a && !b;
}

function toggleAudio() {
  userMedia.then(stream => {
    stream.getAudioTracks().forEach(track => {
      track.enabled = toggleLogic(STATE.audio, track.enabled);
    });
  });
}

function toggleVideo() {
  userMedia.then(stream => {
    stream.getVideoTracks().forEach(track => {
      track.enabled = toggleLogic(STATE.video, track.enabled);
    });
  });
}