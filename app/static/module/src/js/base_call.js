const myVideoWrapper = document.createElement('div');
let myVideo = document.createElement('video');
myVideo.muted = true;
myVideoWrapper.style = 'border: 2px solid red';
myVideoWrapper.append(myVideo);
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
  addVideoStream(myVideoWrapper, stream);
  myPeer.on('call', call => {
    call.answer(stream);
    let parent = document.createElement('div');
    let video = document.createElement('video');
    parent.className = "watcher-item";
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

socket.on('user-kick', userId => {
  window.location.replace('/');
});

myPeer.on('open', id => {
  socket.emit('join-room', room_id, id, user);
  myVideoWrapper.id = id;
});

socket.on('user-disconnected', userId => {
  if (peers[userId]) {
    peers[userId].close();
    document.getElementById(userId).remove();
  }
});

socket.on('user-message', data => {
  makeMessage(data.author, data.text);
});

function connectToNewUser(userId, stream) {
  const call = myPeer.call(userId, stream);
  let parent = document.createElement('div');
  let video = document.createElement('video');
  parent.className = "watcher-item";
  parent.appendChild(video);
  call.on('stream', userVideoStream => {
    parent.id = call.peer;
    addVideoStream(parent, userVideoStream);
  });
  call.on('close', () => {
    parent.remove();
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

function sendMessage(inputId) {
  let messageInput = document.getElementById(inputId);
  let text = messageInput.value;
  if (text === '' || text == null) return false;
  messageInput.value = null;
  socket.emit('user-message', text);
  makeMessage('Я', text);
}

function makeMessage(author, text) {
  let messageEl = document.createElement('div');
  let authorEl = document.createElement('span');
  authorEl.style.fontWeight = 900;
  authorEl.textContent = author;
  messageEl.append(authorEl);
  messageEl.append(text);
  document.getElementById('message-container').appendChild(messageEl);
}