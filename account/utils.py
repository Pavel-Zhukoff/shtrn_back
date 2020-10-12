from school.settings import SMS_SENDER_NAME, SMS_SENDER_API_KEY


def normalize_phone(phone):
    from re import sub
    return '7{}'.format(sub(r"[() +-]", '', phone)[1:])

def normalize_email(email):
    return email.lower().strip()

def send_sms(phone, text):
    import requests
    import json
    url = 'http://api.sms-prosto.ru/' \
          '?method=push_msg&key={}sender_name={}&phone=+{}&text={}&priority=1&format=json' \
        .format(SMS_SENDER_API_KEY, SMS_SENDER_NAME, phone, text)

    response = json.loads(requests.get(url).text)
    if response['response']['msg']['err_code'] == "0":
        return True
    return False

def build_url(*args, **kwargs):
    from django.http import QueryDict
    from django.urls import reverse
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)
    if not params: return url

    qdict = QueryDict('', mutable=True)
    for k, v in params.items():
        if type(v) is list: qdict.setlist(k, v)
        else: qdict[k] = v

    return url + '?' + qdict.urlencode()
