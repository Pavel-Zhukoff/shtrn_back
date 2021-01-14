from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render
from django.utils import timezone

from config import settings
from config.wsgi import sio
from study.models import RoomModel
from study.service import get_user_instance_by_id
from study.utils import set_user_state, user_state_exists, get_user_state


def find_watcher(user_id):
    pass

# SocketIO events
@sio.event
def connect(sid, environ):
    pass


@sio.on('join-room')
def join_room(sid, room_id, user_peer_id, user_id):
    room = RoomModel.objects.filter(id=room_id, start_date__lte=timezone.now(), is_finished=False)
    if room.exists():
        room = room.get()
        user = get_user_instance_by_id(user_id)
        if user not in room.speakers.all() or user not in room.users.all():
            sio.emit('user-disconnected', user_peer_id, room=room_id, skip_sid=sid)
        is_speaker = user in room.speakers.all()
        default_state = {  # Состояния блокировки видео-аудио-чата-доски
                           # по умолчанию все в муте, кроме чата  и спикера
                        'audio': is_speaker,
                        'video': is_speaker,
                        'chat': True,
                        'board': is_speaker,
                    }
        sid_data = {'room_id': room_id,
                    'peer_id': user_peer_id,
                    'user': user,
                    'is_speaker': is_speaker,
                    'state': default_state,
                    }
        sio.enter_room(sid, room_id)
        sio.save_session(sid , sid_data)
        set_user_state(user_peer_id, {'sid': sid, 'state': default_state})
        sio.emit('user-connected', user_peer_id, room=room_id, skip_sid=sid)
        sio.emit('user-state-update', default_state, to=sid)
    else:
        sio.close_room(room_id)


@sio.on('user-state-update')
def user_state_update(sid, user_id, toggle_state):
    if not sio.get_session(sid)['is_speaker']:
        return
    if user_state_exists(user_id) and toggle_state in ['audio', 'video', 'chat', 'board']:
        current_state = get_user_state(user_id)
        current_state['state'].update((toggle_state, not current_state['state'].get(toggle_state)))
        sio.emit('user-state-update', current_state['state'], to=current_state['sid'])
        set_user_state(user_id, current_state)


@sio.on('kick-user')
def kick_user(sid, user_id):
    if not sio.get_session(sid)['is_speaker']:
        return
    if user_state_exists(user_id):
        user_sid = get_user_state(user_id)['sid']
        sio.disconnect(user_sid)


@sio.event
def disconnect(sid):
    session = sio.get_session(sid)
    sio.emit('user-disconnected', session['peer_id'], room=session['room_id'], skip_sid=sid)

#django views
@login_required
def room(request, room_slug):
    room = RoomModel.objects.get(slug=room_slug)
    if room is None:
        return HttpResponseNotFound('Комната не найдена!')
    speakers = list(map(lambda x: x.user, room.speakers.all()))
    watchers = list(map(lambda x: x.user, room.users.all()))
    print(speakers)
    if request.user in speakers:
        view_name = 'room_speaker.html'
    elif request.user in watchers:
        view_name = 'room.html'
    else:
        return HttpResponseForbidden('У вас нет доступа к этой комнате!')
    return render(request, 'study/{}'.format(view_name), {
        'title': 'Комната №{}'.format(room.name),
        'room': room,
        'peerjs_host': settings.PEERJS_SERVER,
        'peerjs_port': settings.PEERJS_PORT,
    })
