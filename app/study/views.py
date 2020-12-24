import redis
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render
from django.utils import timezone

from config import settings
from config.wsgi import sio
from home.models import TeacherModel
from study.models import RoomModel

REDIS_INSTANCE = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@sio.event
def connect(sid, environ):
    pass


@sio.on('join-room')
def join_room(sid, room_id, user_peer_id, user_id):
    room = RoomModel.objects.filter(id=room_id, start_date__lte=timezone.now(), is_finished=False)
    if room.exists():
        room = room.get()
        user = TeacherModel.objects.get(pk=user_id)
        if user not in room.speakers.all() or user not in room.users.all():
            sio.emit('user-disconnected', user_peer_id, room=room_id, skip_sid=sid)
        is_speaker = user in room.speakers.all()
        default_state = { # Состояния блокировки видео-аудио-чата-доски
                        # по умолчанию все в муте, кроме чата  и спикера
                        'audio': is_speaker,
                        'video': is_speaker,
                        'chat': True,
                        'board': is_speaker,
                    }
        sid_date = {'room_id': room_id,
                    'peer_id': user_peer_id,
                    'user': user,
                    'is_speaker': is_speaker,
                    'state': default_state,
                    }
        sio.enter_room(sid, room_id)
        sio.save_session(sid , sid_date)
        sio.emit('user-connected', user_peer_id, room=room_id, skip_sid=sid)
        sio.emit('user-state-update', default_state, to=sid)
    else:
        sio.close_room(room_id)


@sio.event
def disconnect(sid):
    session = sio.get_session(sid)
    sio.emit('user-disconnected', session['peer_id'], room=session['room_id'], skip_sid=sid)

@login_required
def room(request, room_slug):
    room = RoomModel.objects.get(slug=room_slug)
    if room is None:
        return HttpResponseNotFound('Комната не найдена!')
    if request.user not in room.speakers.all():
        view_name = 'room_speaker.html'
    elif request.user not in room.users.all():
        view_name = 'room.html'
    else:
        return HttpResponseForbidden('У вас нет доступа к этой комнате!')
    return render(request, 'study/{}'.format(view_name), {
        'title': 'Комната №{}'.format(room.name),
        'room': room,
        'peerjs_host': settings.PEERJS_SERVER,
        'peerjs_port': settings.PEERJS_PORT,
    })
