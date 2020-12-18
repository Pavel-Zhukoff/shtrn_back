let currentShape;
let currentShapeResize;
let menuNode = document.getElementById('menu');
let trFlag = false;

document.getElementById('delete-button').addEventListener('click', () => {
    currentShape.destroy();
    layer.draw();
});

document.getElementById('resize-button').addEventListener('click', () => {
    const tr = new Konva.Transformer({
        nodes: [currentShape],
        keepRatio: false,
        anchorStroke: 'black',
        borderStroke:'black',
        boundBoxFunc: (oldBox, newBox) => {
            if (newBox.width < 10 || newBox.height < 10) {
                return oldBox;
            }
            return newBox;
        },
    });
    if (trFlag === false) {
        console.log(currentShape)
        layer.add(tr);
        currentShape.on('transform', () => {
            currentShape.setAttrs({
                scaleX: 1,
                scaleY: 1,
                width: currentShape.width() * currentShape.scaleX(),
                height: currentShape.height() * currentShape.scaleY(),
            });
            applyCrop(currentShape.getAttr('lastCropUsed'));
        });
    }
    trFlag = !trFlag;
    layer.draw();
});

window.addEventListener('click', () => {
    menuNode.style.display = 'none';
});

stage.on('contextmenu', function (e) {
    e.evt.preventDefault();
    if (e.target === stage) {
        return;
    }
    currentShape = e.target;
    menuNode.style.display = 'initial';
    let containerRect = stage.container().getBoundingClientRect();
    menuNode.style.top =
        containerRect.top + stage.getPointerPosition().y + 4 + 'px';
    menuNode.style.left =
        containerRect.left + stage.getPointerPosition().x + 4 + 'px';
});