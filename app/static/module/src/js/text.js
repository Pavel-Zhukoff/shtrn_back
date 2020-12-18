function text(x,y) {
    $('#text-input').addClass('active').css({
        'top': y,
        'left': x,
    }).focus()
    // $('#text-input').keypress(function (e) {
    //    if (e.which == 13) {
    //        $('#text-input').removeClass('active')
    //        let text = new Konva.Text({
    //            x: x,
    //            y: y,
    //            text: $('#text-input').val(),
    //            fontSize: 30,
    //            fontFamily: 'Calibri',
    //            fill: 'red'
    //        });
    //        layer.add(text);
    //        stage.add(layer);
    //        layer.draw();
    //        $('#text-input').val('')
    //    }
    // })
    
}