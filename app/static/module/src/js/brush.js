// let isPaint = false;
// let brushMode = '';
// let lastLine;
//
// stage.on('mousedown touchstart', function (e) {
//     isPaint = true;
//     let pos = stage.getPointerPosition();
//     lastLine = new Konva.Line({
//         stroke: '#df4b26',
//         strokeWidth: 5,
//         globalCompositeOperation:
//             brushMode === 'brush' ? 'source-over' : 'destination-out',
//         points: [pos.x, pos.y],
//     });
//     layer.add(lastLine);
// });
//
// stage.on('mouseup touchend', function () {
//     isPaint = false;
// });
//
// stage.on('mousemove touchmove', function () {
//     if (!isPaint) {
//         return;
//     }
//
//     const pos = stage.getPointerPosition();
//     let newPoints = lastLine.points().concat([pos.x, pos.y]);
//     lastLine.points(newPoints);
//     layer.batchDraw();
// });
//
// let eraser = document.getElementById('eraser');
// eraser.addEventListener('click', function () {
//     brushMode = eraser.value;
// });
// let brush = document.getElementById('brush');
// brush.addEventListener('click', function () {
//     brushMode = brush.value;
// });