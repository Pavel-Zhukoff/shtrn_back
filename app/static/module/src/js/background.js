let stage = new Konva.Stage({
    container: 'container',
    width: window.innerWidth,
    height: window.innerHeight,
    draggable: true,
});

stage.on('mousedown', (e) => {
    const isLeft = e.evt.button === 0;
    stage.draggable(!isLeft);
});
let layer = new Konva.Layer();
stage.add(layer);
layer.draw();
