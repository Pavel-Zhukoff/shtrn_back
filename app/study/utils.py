import json

import redis
from django.core.serializers.json import DjangoJSONEncoder
from django.template.defaultfilters import slugify as django_slugify

from config import settings

REDIS_INSTANCE = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e',
                'ю': 'yu',
                'я': 'ya'}
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


def user_state_exists(user_id):
    return REDIS_INSTANCE.exists(user_id)


def get_user_state(user_id):
    if user_state_exists(user_id):
        return json.loads(REDIS_INSTANCE.get(user_id))
    return None


def set_user_state(user_id, state):
    return REDIS_INSTANCE.set(user_id, json.dumps(state, cls=DjangoJSONEncoder))


def delete_user_state(user_id):
    if user_state_exists(user_id):
        return REDIS_INSTANCE.delete(user_id)
    return False