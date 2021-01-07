// $('#text').click(function () {
//     canvas.isDrawingMode = false;
//     // TEXT_FLAG = true;
//     $('canvas').click(function (e) {
//         const x = e.offsetX;
//         const y = e.offsetY;
//         if (TEXT_FLAG === true) {
//             TEXT_FLAG = false;
//             const x = e.offsetX;
//             const y = e.offsetY;
//             $('body').append(`<textarea id="text-input" style="position:absolute;top:${y - 12}px;left:${x}px;background:transparent;border: none;resize: none;font-size: ${TEXT_SIZE}px;color:${TEXT_COLOR}">`)
//             $('#text-input').focus().keydown(function (e) {
//                 if (e.keyCode === 13) {
//                     let content = $('#text-input').val();
//                     console.log(content)
//                     let text = new fabric.IText(content, {
//                         fill: TEXT_COLOR,
//                         fontSize: TEXT_SIZE,
//                     })
//                     canvas.add(text)
//                     $('#text-input').remove();
//                 }
//             })
//         }
//     })
//     var textOptions = {
//         fontSize:16,
//         left:20,
//         top:20,
//         radius:10,
//         borderRadius: '25px',
//         hasRotatingPoint: true
//     };
//
//     var textObject = new fabric.IText('Enter text here...', textOptions);
//
//     canvas.add(textObject).setActiveObject(textObject);
//     canvas.renderAll()
//
// })
//
//
// $('#pen').click(function () {
//     TEXT_FLAG = false;
// })
