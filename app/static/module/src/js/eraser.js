function eraser() {
    ERASER_FLAG = true;
    $(document).click(function (e) {
        let x =e.clientX
        let y =e.clientY
        ctx.clearRect(x,y,1,1)
    })
}
