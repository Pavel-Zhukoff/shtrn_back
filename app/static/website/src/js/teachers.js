$(document).ready(function () {
    function setCardHeight() {
        $('.teachers__slider__card').css({
            height: $('.teachers__slider__card').width() + 4 + $('.teachers__slider__title').height()
        })
        $('.teachers__slider__image img, .teachers__slider__image').css({
            height: $('.teachers__slider__card').width() + 4
        })
        $('.teachers__wrapper__slider').css({
            height: $('.teachers__container').height() - $('.teachers__container__title').height() - 50
        })
        $('.teachers__content__info').css({
            height: $('.teachers__content__info').width()
        })
    }
    $(window).resize(setCardHeight())
    $(window).resize(()=>{
        setCardHeight()
    })
    function setLastnameUppercase() {
        let strings = [];
        $('.teachers__slider__title').each(function (index) {
            strings.push($(this).text().replace('\n','').trim().split(' '))
            let string = strings[index][0].toUpperCase() + '<br>' + strings[index][1] + ' '  + strings[index][2]
            $(this).html(string)
        })
    }
    setLastnameUppercase()


    function changeContent() {
        $('.teachers__slider__image img').click(function () {
            $('.teachers__slider__image img').removeClass('active')
            $(this).addClass('active')
            $('.teachers__content__info img').attr('src', $(this).attr('src'));
            $('.teachers__content__name h3').html($(this).parent().next().html())
        })
    }
    changeContent()
})
