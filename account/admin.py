from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from account.models import ReviewModel, User, StudentModel


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('get_short_name', 'phone', 'email', 'show_children')

    fieldsets = (
        ('Пользователь', {
            'fields': ('last_name', 'first_name', 'third_name',),
            'classes': (),
        }),
        ('Контактная информация', {
            'fields': ('phone', 'email',),
        }),
        ('Дополнительно', {
            'fields': ('is_active', 'password', 'groups', 'is_staff', 'is_superuser', 'last_login'),
            'classes': ('collapse',),
        })
    )

    ordering = ('register_date', )
    search_fields = ('last_name', 'first_name', 'third_name', 'email', 'phone',)

    add_fieldsets = (
        ('Данные для входа', {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password1', 'password2', ),
        }),
    )

    def show_children(self, obj):
        count = obj.studentmodel_set.count()
        url = (
            reverse('admin:account_studentmodel_changelist')
            + '?'
            + urlencode({'user__id': f'{obj.id}'})
        )
        return format_html('<a href="{}">{} детей</a>', url, count)

    show_children.short_description = 'Дети'

    class CreationForm(UserCreationForm):

        def clean(self):
            from account.utils import normalize_phone, normalize_email
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
    pass


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
