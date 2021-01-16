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
  setAudio(STATE.audio);
  setVideo(STATE.video);
});
userMedia.then(stream => {
  addVideoStream(myVideo, stream);
  myPeer.on('call', call => {
    let parent = document.createElement('div');
    let video = document.createElement('video');
    parent.className = "watcher-item";
    parent.appendChild(video);
    call.answer(stream);
    call.on('stream', userVideoStream => {
      parent.id = call.peer;
      addVideoStream(video, userVideoStream);
    });
  });

  socket.on('user-connected', userId => {
    console.log(userId);
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

socket.on('user-chat-init', messages => {
  messages.forEach(message => {
    makeMessage(message[0], message[1], user === message[2]);
  })
});

function connectToNewUser(userId, stream) {
  const call = myPeer.call(userId, stream);
  let parent = document.createElement('div');
  let video = document.createElement('video');
  parent.className = "watcher-item";
  parent.appendChild(video);
  call.on('stream', userVideoStream => {
    parent.id = call.peer;
    addVideoStream(video, userVideoStream);
  });
  call.on('close', () => {
    parent.remove();
  });

  peers[userId] = call;
}
// Добавляет видео в сетку
function addVideoStream(video, stream) {
  video.srcObject = stream;
  video.addEventListener('loadedmetadata', () => {
    video.play();
  });
  videoGrid.append(video.parentNode);
}

function toggleLogic(a, b) {
  return a && !b;
}

function setAudio(enabled) {
  userMedia.then(stream => {
    stream.getAudioTracks().forEach(track => {
      track.enabled = enabled;
    });
  });
}

function setVideo(enabled) {
  userMedia.then(stream => {
    stream.getVideoTracks().forEach(track => {
      track.enabled = enabled;
    });
  });
}

function toggleAudio() {
  userMedia.then(stream => {
    stream.getVideoTracks().forEach(track => {
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

function sendMessage(inputId, author) {
  let messageInput = document.getElementById(inputId);
  let text = messageInput.value;
  if (text === '' || text == null) return false;
  messageInput.value = null;
  socket.emit('user-message', text);
  makeMessage(author, text, true);
}

function makeMessage(author, text, my) {
  let messageEl = document.createElement('div');
  let authorEl = document.createElement('span');
  authorEl.style.fontWeight = 900;
  authorEl.textContent = author;
  if (my) {
    messageEl.style.textAlign = 'right';
    authorEl.style.color = 'red';
  }
  messageEl.append(authorEl);
  messageEl.append(text);
  document.getElementById('message-container').appendChild(messageEl);
}