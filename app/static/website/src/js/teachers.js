$(document).ready(function () {
    let teachersResult = {}
    $.ajax({
        type: 'get',
        dataType: 'json',
        url: '/teachers/data',
        data: {},
        success: function (data) {
            teachersResult = data;
            return data
        }
    }).done(function () {
        teachers()
    })
    function teachers() {
        function outTeachersList(data) {
            $.each(data, (index, value) => {
                $('.teachers__wrapper__slider').html(`
                    <div class="teachers__slider__card" id="${index}" sex="${data[index].sex}">
                      <div class="teachers__slider__image">
                         <img src="/media/${data[index].photo}"
                                 alt="${data[index].name}">
                     </div>
                        <div class="teachers__slider__title">
                            ${data[index].name}
                        </div>
                    </div>
                `)
            })
        }
        outTeachersList(teachersResult)
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
        $(window).resize(() => {
            setCardHeight()
        })
        function setLastnameUppercase() {
            let strings = [];
            $('.teachers__slider__title').each(function (index) {
                strings.push($(this).text().replace('\n', '').trim().split(' '))
                let string = strings[index][0].toUpperCase() + '<br>' + strings[index][1] + ' ' + strings[index][2]
                $(this).html(string)
            })
        }
        setLastnameUppercase()
        function loadSetContent(data) {
            $('.teachers__slider__image img').eq(0).addClass('active')
            $('.teachers__content__info img').attr('src', $('.teachers__slider__image img').eq(0).attr('src'));
            $('.teachers__content__name h3').html(data[0].name)
            $('.teachers__content__position h2').html(data[0].job)
            $('.content__description__item.education').html(`
                 <div class="description__item__title ">
                         Образование:
                     </div>
                     <div class="description__item__text">
                         ${data[0].education}
                     </div>
                 `)
            $('.content__description__item.experience ').html(`
                <div class="description__item__title ">
                        Педагогический стаж:
                    </div>
                    <div class="description__item__text">
                        ${data[0].experience}
                    </div>
                `)
        }
        loadSetContent(teachersResult)
        function changeContent(data) {
            $('.teachers__slider__image img').click(function () {
                if (data[$(this).parent().parent().attr('id')].sex === 'f') {
                    $('.teachers').animate({
                        background: 'radial-gradient(circle, rgba(78,171,225,0.6) 15%, rgba(146,82,156,0.9) 70%)'
                },200)
                } else {
                    $('.teachers').animate({
                        background: 'radial-gradient(circle, rgba(146,82,156,0.6) 40%, rgba(78,171,225,0.9) 100%)'
                    },200)
                }
                $('.teachers__slider__image img').removeClass('active')
                $(this).addClass('active')
                $('.teachers__content__info img').attr('src', $(this).attr('src'));
                $('.teachers__content__name h3').html(data[$(this).parent().parent().attr('id')].name)
                $('.teachers__content__position h2').html(data[$(this).parent().parent().attr('id')].job)
                $('.content__description__item.education').html(`
                <div class="description__item__title ">
                        Образование:
                    </div>
                    <div class="description__item__text">
                        ${data[$(this).parent().parent().attr('id')].education}
                        
                    </div>
                `)
                $('.content__description__item.experience ').html(`
                <div class="description__item__title ">
                        Педагогический стаж:
                    </div>
                    <div class="description__item__text">
                        ${data[$(this).parent().parent().attr('id')].experience}
                        
                    </div>
                `)
            })
        }
        changeContent(teachersResult)
    }
})
