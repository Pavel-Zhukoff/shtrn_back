import redis
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render

from config import settings
from config.wsgi import sio
from study.models import RoomModel

REDIS_INSTANCE = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@sio.event
def connect(sid, environ):
    print(sid)


@sio.on('join-room')
def join_room(sid, room_id, user_peer_id):
    if RoomModel.objects.filter(id=room_id, available=True).exists():
        sio.enter_room(sid, room_id)
        sio.save_session(sid , {'room_id': room_id, 'peer_id': user_peer_id})
        sio.emit('user-connected', user_peer_id, room=room_id, skip_sid=sid)
    else:
        sio.close_room(room_id)


@sio.event
def disconnect(sid):
    session = sio.get_session(sid)
    sio.emit('user-disconnected', session['peer_id'], room=session['room_id'], skip_sid=sid)

@login_required
def room(request, room_slug):
    room = RoomModel.objects.get(slug=room_slug)
    print(REDIS_INSTANCE)
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
