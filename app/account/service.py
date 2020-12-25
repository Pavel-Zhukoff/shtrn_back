import random

from account.models import VerificationModel, User
from account.utils import normalize_phone, send_sms


def create_user_verification(data):
    """Создает код подтверждения пользователя"""
    phone = normalize_phone(data.get('phone'))
    code = random.randint(10000000, 99999999) % 10000000
    verify = VerificationModel()
    verify.phone = phone
    verify.code = code
    verify.save()
    return phone, code


def verify_user(code, phone):
    """ Проверяет верификацию пользователя и возвращает нового пользователя в случае успеха"""
    verification = VerificationModel.objects.get(phone=phone)
    if code == verification.code:
        user = User.objects.create_user(phone, verification.code)
        user.save()
        verification.delete()
        return user
    return None


def change_password(user, password):
    user.set_password(password)
    user.save()