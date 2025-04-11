from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from DjangoFitnessApp.accounts.forms import RegisterForm, AppUserChangeForm
from DjangoFitnessApp.accounts.models import Profile


# Register your models here.
UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture', )


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    add_form = RegisterForm
    form = AppUserChangeForm

    list_display = (
        "pk", "is_staff", "username", "email", "is_active"
    )

    list_filter = (
        "is_staff", "is_active",
    )

    search_fields = (
        "email", "username",
    )

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

