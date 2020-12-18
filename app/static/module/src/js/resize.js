function getCrop(image, size, clipPosition = 'center-middle') {
    const width = size.width;
    const height = size.height;
    const aspectRatio = width / height;

    let newWidth;
    let newHeight;

    const imageRatio = image.width / image.height;

    if (aspectRatio >= imageRatio) {
        newWidth = image.width;
        newHeight = image.width / aspectRatio;
    } else {
        newWidth = image.height * aspectRatio;
        newHeight = image.height;
    }

    let x = 0;
    let y = 0;

    return {
        cropX: x,
        cropY: y,
        cropWidth: newWidth,
        cropHeight: newHeight,
    };
}

function applyCrop(pos) {
    const img = layer.findOne('.image');
    img.setAttr('lastCropUsed', pos);
    const crop = getCrop(
        img.image(),
        { width: img.width(), height: img.height() },
        pos
    );
    img.setAttrs(crop);
    layer.draw();
}
