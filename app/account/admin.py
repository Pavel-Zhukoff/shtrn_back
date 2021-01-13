from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from account.models import ReviewModel, User, StudentModel
from account.models.parent import ParentModel
from account.utils import normalize_phone, normalize_email


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('get_short_name', 'phone', 'email')
    fieldsets = (
        ('Пользователь', {
            'fields': ('last_name', 'first_name', 'third_name', ),
            'classes': (),
        }),
        ('Контактная информация', {
            'fields': ('phone', 'email',),
        }),
        (None, {
            'fields': ('register_date', ),
        }),
        ('Дополнительно', {
            'fields': ('is_active', 'password', 'groups', 'is_staff', 'is_superuser', 'last_login'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('register_date', )
    ordering = ('register_date', 'last_name', 'first_name', 'third_name', )
    search_fields = ('last_name', 'first_name', 'third_name', 'email', 'phone',)
    add_fieldsets = (
        ('Персональные данные', {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'email',),
        }),
        ('Данные для входа', {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', ),
        }),
    )


    class CreationForm(UserCreationForm):

        def clean(self):
            cleaned_data = self.cleaned_data
            phone = normalize_phone(cleaned_data['phone'])
            email = normalize_email(cleaned_data['email'])

            if phone and User.objects.filter(phone=phone):
                self.add_error('phone', 'Пользователь с данным номером телефона уже зарегистрирован')
            elif email and User.objects.filter(email=email):
                self.add_error('email', 'Пользователь с данной электронной почтой уже зарегистрирован')

            return cleaned_data

    add_form = CreationForm


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_short_name', 'phone', 'year_of_study', 'get_parent', )
    search_fields = ('last_name', 'first_name', 'third_name', 'phone',)
    list_filter = (
        ('year_of_study', admin.ChoicesFieldListFilter),
    )

    def get_parent(self, obj):
        url = (
                reverse('admin:account_user_changelist')
                + '?'
                + urlencode({'id': f'{obj.parent.id}'})
        )
        return format_html('<a href="{}">{}</a>', url, obj.parent.get_short_name())

    get_parent.short_description = 'Родитель'


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(ParentModel)

admin.site.unregister(Group)
