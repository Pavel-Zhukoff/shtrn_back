videoGrid.childNodes.forEach((el, i) => {
    if (i !== 0) {
        const toggleAudioBtn = document.createElement('button');
        const toggleVideoBtn = document.createElement('button');
        const kickBtn = document.createElement('button');
        toggleAudioBtn.textContent = 'Вкл\\Выкл аудио';
        toggleVideoBtn.textContent = 'Вкл\\Выкл видео';
        kickBtn.textContent = 'Отключить пользователя';


        el.appendChild(toggleAudioBtn);
        el.appendChild(toggleVideoBtn);
        el.appendChild(kickBtn);
    }
});