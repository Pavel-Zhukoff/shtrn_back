$(document).ready(function () {
    function getButtonState() {
        $('.schedule__return__btn').attr('data-state','location') ? $('.schedule__return__btn').removeClass('disabled') : $('.schedule__return__btn').addClass('disabled');
    }
    let scheduleData = {
        'location': '',
        'class': '',
        'subject': '',
        'day': '',
    }
    $('.schedule__item__button').click(function () {
        $('.schedule__item__classes').css({
            'opacity':'1',
        })
        getButtonState()
        $('.schedule__return__btn').attr('data-state','class')
        scheduleData.location = $(this).attr('data-location')
        console.log(scheduleData)
        $(this).parent().addClass('slide');
        $('.schedule__item__button').eq(0).animate({
            'top': '36px',
        }, 200)
        $('.schedule__item__button').eq(1).animate({
            'bottom': '36px',
        }, 200)
        setTimeout(function () {
            $('.schedule__item__button').animate({
                'color': 'transparent',
                'opacity': 0,
            }, 200)
            $('.schedule__item__locations').removeClass('active')
        }, 400)

        setTimeout(function () {
            $('.schedule__item__classes').addClass('active')
            $('.schedule__classes__button').animate({
                'left': 0,
                'right': 0,
                'top': 0,
                'bottom': 0,
            }, 100)
        }, 600)

    })
    $('.schedule__classes__button').click(function () {
        getButtonState()
        $('.schedule__return__btn').attr('data-state','subject')
        scheduleData.class = $(this).attr('data-class')
        console.log(scheduleData)
        $('.schedule__classes__button').eq(0).css({
            'left': '138px',
            'top': '100px',
        })
        $('.schedule__classes__button').eq(1).css({
            'left': '54px',
            'top': '100px',
        })
        $('.schedule__classes__button').eq(2).css({
            'left': '-32px',
            'top': '100px',
        })
        $('.schedule__classes__button').eq(3).css({
            'top': '100px',
            'left': '-119px',
        })
        $('.schedule__classes__button').eq(4).css({
            'top': '9px',
            'left': '138px',
        })
        $('.schedule__classes__button').eq(5).css({
            'top': '9px',
            'left': '54px',
        })
        $('.schedule__classes__button').eq(6).css({
            'top': '9px',
            'left': '-30px',
        })
        $('.schedule__classes__button').eq(7).css({
            'top': '9px',
            'left': '-117px',
        })
        $('.schedule__classes__button').eq(8).css({
            'top': '-82px',
            'left': '139px',
        })
        $('.schedule__classes__button').eq(9).css({
            'top': '-82px',
            'left': '54px',
        })
        $('.schedule__classes__button').eq(10).css({
            'top': '-82px',
            'left': '-31px',
        })
        setTimeout(function () {
            $('.schedule__item__classes').animate({
                'color': 'transparent',
                'opacity': 0,
            }, 50)
            $('.schedule__item__classes').removeClass('active')
        }, 250)
        setTimeout(function () {
            $('.schedule__item__classes').css({
                'opacity': 1,
            }, 1)
        }, 250)
        setTimeout(function () {
            $('.schedule__item__subjects').addClass('active')
            $('.subject__button__wrapper').animate({
                'left': 0,
                'right': 0,
                'top': 0,
                'bottom': 0,
            }, 100)
        }, 250)
    })
    $('.subject__button').click(function () {
        $('.schedule__return__btn').attr('data-state','day')
        scheduleData.subject = $(this).attr('data-subject')
        console.log(scheduleData)
        $('.subject__button__wrapper').eq(0).animate({
            'top': '175px'
        }, 200)
        $('.subject__button__wrapper').eq(1).animate({
            'top': '100px'
        }, 200)
        $('.subject__button__wrapper').eq(2).animate({
            'top': '35px'
        }, 200)
        $('.subject__button__wrapper').eq(3).animate({
            'top': '-40px'
        }, 200)
        $('.subject__button__wrapper').eq(4).animate({
            'top': '-115px'
        }, 200)
        $('.subject__button__wrapper').eq(5).animate({
            'top': '-190px'
        }, 200)
        setTimeout(function () {
            $('.schedule__item__subjects ').removeClass('active')
        }, 200)
        setTimeout(function () {
            $('.schedule__item__days').addClass('active')
        }, 200)
        setTimeout(function () {
            $('.schedule__item__subjects ').removeClass('active')
            $('.schedule__item__days').addClass('active')
            $('.schedule__days__button').animate({
                'left':0,
                'right':0,
                'top':0,
                'bottom':0,
            },200)
        },200)
    })
    $('.schedule__days__button').click(function () {
        scheduleData.day = $(this).attr('data-day')
        console.log(scheduleData)
    })
    $('.schedule__return__btn').click(function () {
        console.log($('.schedule__return__btn').attr('data-state'))
        if($(this).attr('data-state')==='class') {
            scheduleData.location = '';
            console.log(scheduleData)
            $('.schedule__classes__button').eq(0).css({
                'left': '138px',
                'top': '100px',
            })
            $('.schedule__classes__button').eq(1).css({
                'left': '54px',
                'top': '100px',
            })
            $('.schedule__classes__button').eq(2).css({
                'left': '-32px',
                'top': '100px',
            })
            $('.schedule__classes__button').eq(3).css({
                'top': '100px',
                'left': '-119px',
            })
            $('.schedule__classes__button').eq(4).css({
                'top': '9px',
                'left': '138px',
            })
            $('.schedule__classes__button').eq(5).css({
                'top': '9px',
                'left': '54px',
            })
            $('.schedule__classes__button').eq(6).css({
                'top': '9px',
                'left': '-30px',
            })
            $('.schedule__classes__button').eq(7).css({
                'top': '9px',
                'left': '-117px',
            })
            $('.schedule__classes__button').eq(8).css({
                'top': '-82px',
                'left': '139px',
            })
            $('.schedule__classes__button').eq(9).css({
                'top': '-82px',
                'left': '54px',
            })
            $('.schedule__classes__button').eq(10).css({
                'top': '-82px',
                'left': '-31px',
            })
            setTimeout(function () {
                $('.schedule__item__classes').animate({
                    'color': 'transparent',
                    'opacity': 0,
                }, 50)
                $('.schedule__item__classes').removeClass('active')
            }, 250)
            setTimeout(function () {
                $('.schedule__item__locations').addClass('active')
                $('.schedule__item__button').eq(0).animate({
                    'top': 0,
                    'opacity':1,
                }, 100)
                $('.schedule__item__button').eq(1).animate({
                    'bottom': 0,
                    'opacity':1,
                }, 100)
            }, 250)
            $('.schedule__return__btn').attr('data-state','location')
            $('.schedule__return__btn').addClass('disabled')

        } else if ($(this).attr('data-state')==='subject') {
            $('.subject__button__wrapper').eq(0).animate({
                'top': '175px'
            }, 200)
            $('.subject__button__wrapper').eq(1).animate({
                'top': '100px'
            }, 200)
            $('.subject__button__wrapper').eq(2).animate({
                'top': '35px'
            }, 200)
            $('.subject__button__wrapper').eq(3).animate({
                'top': '-40px'
            }, 200)
            $('.subject__button__wrapper').eq(4).animate({
                'top': '-115px'
            }, 200)
            $('.subject__button__wrapper').eq(5).animate({
                'top': '-190px'
            }, 200)
            setTimeout(function () {
                $('.schedule__item__subjects ').removeClass('active')
            }, 200)
            setTimeout(function () {
                $('.schedule__item__classes').addClass('active')
            }, 200)
            setTimeout(function () {
                $('.schedule__item__classes').css({
                    'opacity': '1',
                })
            })
            setTimeout(function () {
                $('.schedule__classes__button').animate({
                    'left': 0,
                    'right': 0,
                    'top': 0,
                    'bottom': 0,
                    'opacity':1,
                }, 100)
            }, 250)
            $('.schedule__return__btn').attr('data-state','class')
            scheduleData.class = '';
            console.log(scheduleData)
        } else if ($(this).attr('data-state')==='day') {
            scheduleData.day = '';
            scheduleData.subject = '';
            console.log(scheduleData)
        }
    })
    $('.modal__close__button').click(function () {$('.modal').attr('data-target',$(this).attr('data-target')).addClass('disabled')})
    $('.schedule__days__button').click(function () {$('.schedule__modal').removeClass('disabled')})
    $('.subject__button__wrapper svg').click(function () {$('.schedule__modal').removeClass('disabled')})
})
