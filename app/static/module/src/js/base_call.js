const myVideo = document.createElement('video');
myVideo.style = 'border: 2px solid red';
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
    const video = document.createElement('video');
    call.on('stream', userVideoStream => {
      video.id = call.peer;
      addVideoStream(video, userVideoStream);
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
});

function connectToNewUser(userId, stream) {
  const call = myPeer.call(userId, stream);
  const video = document.createElement('video');
  call.on('stream', userVideoStream => {
    video.id = call.peer;
    addVideoStream(video, userVideoStream);
  });
  call.on('close', () => {
    video.remove();
  });

  peers[userId] = call;
}
// Добавляет видео в сетку
function addVideoStream(video, stream) {
  video.srcObject = stream;
  video.addEventListener('loadedmetadata', () => {
    video.play();
  });
  videoGrid.append(video);
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