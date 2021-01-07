function toggleToolbar() {
    let TOGGLE_FLAG = false;
    $('.toolbar.toggles').click(function () {
        TOGGLE_FLAG = !TOGGLE_FLAG;
        $('.toolbar.toggles img').toggleClass('active')
        $('#toolbar').toggle("slide",400);
        if (TOGGLE_FLAG === true) {
            $('.toolbar.toggles').animate({
                left: 0
            },399)
        } else {
            $('.toolbar.toggles').animate({
                left: 68
            },401)
        }
    })
}

function toggleCalc() {
    let TOGGLE_FLAG = false;
    $('.calc.toggles').click(function () {
        TOGGLE_FLAG = !TOGGLE_FLAG;
        if (TOGGLE_FLAG === true) {
            $('#calc').slideUp()
            $('.calc.toggles').animate({
                bottom: 0
            },399)
        } else {
            $('#calc').slideDown()
            $('.calc.toggles').animate({
                bottom: 343
            },401)
        }
    })
}

function fullScreen(){
    $('#fullscreen').click(function () {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    })
}
function endLesson() {
    $('.finish__button').click(function () {
        $('#finishLesson').addClass('active')
    })
    $('#cancel__finish').click(function () {
        $('#finishLesson').removeClass('active')
    })
}


toggleToolbar();
toggleCalc();
fullScreen();
endLesson();
