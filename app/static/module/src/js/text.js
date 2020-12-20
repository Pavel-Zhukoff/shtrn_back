$('#text').click(function () {
    canvas.isDrawingMode = false;
    let text = new fabric.IText('Hello Hello Hello Hello\n Hello Hello Hello Hello ',{
        fill: TEXT_COLOR,
        fontSize: TEXT_SIZE,
    })
    canvas.add(text)
})
