const canvas = new fabric.Canvas("c", {
    hoverCursor: 'pointer',
    selectionBorderColor: 'green',
    backgroundColor: null
});

let ctx = canvas.getContext('2d');


$('#ctxClear').click(function () {
    canvas.clear()
})
