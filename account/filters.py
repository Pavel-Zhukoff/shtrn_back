from django.contrib import admin

from account.models import StudentModel


class StudyYearFilter(admin.SimpleListFilter):

    title = 'Класс'

    def lookups(self, request, model_admin):
        return StudentModel.SCHOOL_CLASSES

    def queryset(self, request, queryset):
        return StudentModel.objects.filter(year_of_study=self.value())
