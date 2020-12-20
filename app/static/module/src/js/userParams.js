let BRUSH_COLOR = '#212121';
let TEXT_COLOR = '#212121';
let TEXT_SIZE = '18'
let BRUSH_FLAG = false;
let ERASER_FLAG = false;
let BACKGROUND_FLAG = false;
function loadColors() {
    $('.colors .color').each((index,value)=>{
        $('.colors .color').eq(index).css({
            backgroundColor: value.dataset.color,
        });
    })
    $('.text-colors .color').each((index,value)=>{
        $('.text-colors .color').eq(index).css({
            backgroundColor: value.dataset.color,
        });
    })
}
function setColors() {
    $('.colors .color').click(function(){
        BRUSH_COLOR = $(this).data('color');
        canvas.freeDrawingBrush.color = BRUSH_COLOR;
    });
    $('.text-colors .color').click(function(){
        TEXT_COLOR = $(this).data('color');
    });
}
function loadSizes() {
    $('.text-sizes .size').each((index,value)=>{
        $('.text-sizes .size').eq(index).text(value.dataset.size);
    })
}
function setSizes() {
    $('.text-sizes .size').click(function(){
        TEXT_SIZE = $(this).data('size');
    });
}
loadColors();
setColors();
loadSizes();
setSizes();
