from atexit import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreatoionForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatoionForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] += ("age",)

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'age',
            ),
        }),
    )


