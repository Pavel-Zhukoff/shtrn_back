
function setText() {
    let x = 0;
    let y = 0;
    $('#layout').click(function (e) {
        x = e.pageX;
        y = e.pageY;
        $('#text-input').css({
            left: screen.width - (screen.width - (x - $('#text-input').innerWidth() / 2)) + 'px',
            top: screen.height - (screen.height - (y - $('#text-input').innerHeight() / 2)) + 'px',
        }).addClass('active').focus()
    })
    $('#text-input').keypress(function (e) {
        let canvas = document.getElementById('layout');
        let ctx = canvas.getContext('2d')
        if (e.which == 13) {
            let text = $('#text-input').val();
            console.log(text)
            $('#text-input').val('').removeClass('active')
            ctx.fillStyle = "#435a6b";
            ctx.font = "42px Arial";
            // ctx.fillText(text, screen.width - (screen.width - (x - $('#text-input').innerWidth() / 2)), screen.height - (screen.height - y));
            ctx.fillText(text, 500, 350);
        }
    })
}
