function deleteObjects(){
    window.deleteObject = function() {
        canvas.getActiveObject().remove();
    }
    // var activeObject = canvas.getActiveObject(),
    //     activeGroup = canvas.getActiveGroup();
    // if (activeObject) {
    //     if (confirm('Are you sure?')) {
    //         canvas.remove(activeObject);
    //     }
    // }
    // else if (activeGroup) {
    //     if (confirm('Are you sure?')) {
    //         var objectsInGroup = activeGroup.getObjects();
    //         canvas.discardActiveGroup();
    //         objectsInGroup.forEach(function(object) {
    //             canvas.remove(object);
    //         });
    //     }
    // }
}


$('html').keydown(function (e) {
    if (e.keyCode === 46) {
        let activeObject = canvas.getActiveObjects();
        canvas.discardActiveObject();
        canvas.remove(...activeObject);
    }
})
