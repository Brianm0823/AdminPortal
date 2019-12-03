from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
                           'groups', 'user_permissions')
        else:
            # modify these to suit the fields you want your
            # staff user to be able to edit
            perm_fields = ('is_active', 'is_staff', 'groups')

        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]

admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Permission)
admin.site.unregister(Site)