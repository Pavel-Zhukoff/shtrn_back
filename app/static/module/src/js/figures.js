let itemURL = '';
document
    .getElementById('drag-figures')
    .addEventListener('dragstart', function (e) {
        itemURL = e.target.src;
    });

let con = stage.container();
con.addEventListener('dragover', function (e) {
    e.preventDefault();
});

con.addEventListener('drop', function (e) {
    e.preventDefault();
    stage.setPointersPositions(e);

    Konva.Image.fromURL(itemURL, function (image) {
        layer.add(image);
        image.setAttrs({
            name: 'image',
        })
        image.position({
           x: e.clientX - image.attrs.image.width/2,
           y: e.clientY - image.attrs.image.height/2,
        });
        image.zIndex(900000)
        image.draggable(true);

        layer.draw();
    });

});

