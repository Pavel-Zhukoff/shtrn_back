let BRUSH_COLOR = '#212121';
let BRUSH_SIZE = 1;
let TEXT_COLOR = '#212121';
let TEXT_SIZE = '18'
let BRUSH_FLAG = false;
let ERASER_FLAG = false;
let BACKGROUND_FLAG = false;
let TEXT_FLAG = false;



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
function setBrushColors() {
    $('.feltTipPen .colors .color').click(function(){
        BRUSH_COLOR = $(this).data('color');
        canvas.freeDrawingBrush.color = BRUSH_COLOR;
        $('.feltTipPen .colors .color').removeClass('active')
        $(this).addClass('active')
    });
    // $('.text-colors .color').click(function(){
    //     TEXT_COLOR = $(this).data('color');
    // });
}
function setBrushSize() {
    $('.feltTipPen .sizes .size').click(function () {
        BRUSH_SIZE = $(this).data('size');
        canvas.freeDrawingBrush.width = BRUSH_SIZE;
        $('.feltTipPen .sizes .size').removeClass('active')
        $(this).addClass('active')
    })
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
setBrushColors();
loadSizes();
setSizes();
setBrushSize()
