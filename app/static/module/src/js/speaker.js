socket.on('user-connected', userId => {
    const el = document.getElementById(userId);
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
    toggleAudioBtn.onclick = socket.emit('user-state-update', userId, 'audio');
    toggleVideoBtn.onclick = socket.emit('user-state-update', userId, 'video');
    toggleChatBtn.onclick = socket.emit('user-state-update', userId, 'chat');
    toggleBoardBtn.onclick = socket.emit('user-state-update', userId, 'board');
    kickBtn.onclick = socket.emit('kick-user', userId);

    el.appendChild(toggleAudioBtn);
    el.appendChild(toggleVideoBtn);
    el.appendChild(kickBtn);
});