from account.models import StudentModel
from home.models import TeacherModel


def get_user_instance_by_id(user_id):
    """ return user with its type by user_id """

    if TeacherModel.objects.filter(user__id=user_id).exists():
        return TeacherModel.objects.get(user__id=user_id)
    elif StudentModel.objects.filter(user__id=user_id).exists():
        return StudentModel.objects.get(user__id=user_id)
    return None