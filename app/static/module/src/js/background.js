$('#background').click(function () {
    cellBg()
})
function cellBg() {
    console.log(BACKGROUND_FLAG)
    console.log(canvas.backgroundImage)
    if (!BACKGROUND_FLAG) {
        const imageUrl = "https://images.unsplash.com/photo-1608354580409-0ec9a4f8b163?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80";
        canvas.setBackgroundImage(imageUrl, canvas.renderAll.bind(canvas), {
            backgroundImageOpacity: 0.5,
            backgroundImageStretch: false
        });
    } else {
        canvas.backgroundImage = 0;
        canvas.backgroundColor = '#eee';
        canvas.renderAll();
    }
    BACKGROUND_FLAG = !BACKGROUND_FLAG;
    console.log(BACKGROUND_FLAG)
}
