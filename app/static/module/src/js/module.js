$(document).ready(function () {
    let x = 0;
    let y = 0;
    let canvas = new Canvas(screen.width, screen.height)
    console.log(canvas)
    $(window).resize(function () {
        canvas = new Canvas(screen.width, screen.height)
        console.log(canvas.setSize())
    })
    $('#layout').click(function (e){
        x = e.pageX;
        y = e.pageY;
        let coords = new Coords(x,y)
        console.log(coords.getCoords())
    })
})