const canvas = new fabric.Canvas("c", {
    hoverCursor: 'pointer',
    selectionBorderColor: 'green',
    backgroundColor: null
});

let ctx = canvas.getContext('2d');
console.log(canvas.freeDrawingBrush)
$('#background').click(function () {
    cellBg()
})

