var mutationObserver = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
      const el = mutation.addedNodes[mutation.addedNodes.length - 1];
    const toggleAudioBtn = document.createElement('button');
    const toggleVideoBtn = document.createElement('button');
    const toggleChatBtn = document.createElement('button');
    const toggleBoardBtn = document.createElement('button');
    const kickBtn = document.createElement('button');
    toggleAudioBtn.textContent = 'Вкл\\Выкл аудио';
    toggleVideoBtn.textContent = 'Вкл\\Выкл видео';
    toggleChatBtn.textContent = 'Вкл\\Выкл чат';
    toggleBoardBtn.textContent = 'Вкл\\Выкл доску';
    kickBtn.textContent = 'Отключить пользователя';
    toggleAudioBtn.onclick = function () {
      socket.emit('user-state-update', el.id, 'audio')
    };
    toggleVideoBtn.onclick = function () {
      socket.emit('user-state-update', el.id, 'video')
    };
    toggleChatBtn.onclick = function () {
      socket.emit('user-state-update', el.id, 'chat')
    };
    toggleBoardBtn.onclick = function () {
      socket.emit('user-state-update', el.id, 'board')
    };
    kickBtn.onclick = function () {
      socket.emit('kick-user', el.id)
    };

    el.appendChild(toggleAudioBtn);
    el.appendChild(toggleVideoBtn);
    el.appendChild(toggleChatBtn);
    el.appendChild(toggleBoardBtn);
    el.appendChild(kickBtn);
  });
});
mutationObserver.observe(videoGrid, {childList: true});
