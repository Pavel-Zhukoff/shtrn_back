$(document).ready(function () {
    let x = 0;
    let y = 0;
    $('#layout').click(function (e){
        x = e.pageX;
        y = e.pageY;
        let coords = new Coords(x,y)
        console.log(coords.getCoords())
    })
})