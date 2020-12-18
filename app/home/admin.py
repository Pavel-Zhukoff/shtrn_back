from django.contrib import admin

from home.models import AdviceModel, EventModel, NewsModel, SchoolModel, ScheduleModel, SubjectModel, TeacherModel, \
    TextbookModel, StudyGroupModel


@admin.register(AdviceModel)
class AdviceAdmin(admin.ModelAdmin):
    pass


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(SchoolModel)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(ScheduleModel)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(SubjectModel)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(TextbookModel)
class ATextbookAdmin(admin.ModelAdmin):
    pass


@admin.register(StudyGroupModel)
class StudyGroupAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = 'Админпанель сайта школы Штерн'
