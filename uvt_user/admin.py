from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .models import UvtUser

class UvtUserInline(admin.StackedInline):
    model = UvtUser
    readonly_fields = ['first_name', 'full_name', 'ANR', 'email']
    verbose_name_plural = 'Uvt user information'

class UserAdmin(BaseUserAdmin):
    save_on_top = True
    inlines = [UvtUserInline]
    list_display = ['username', 'user_type', 'first_name', 'last_name', 'anr', 'full_name', 'email', 'is_staff']

    def user_type(self, user):
        if hasattr(user, 'uvt_user'):
            return 'UvT user'
        else:
            return 'Regular user'

    def anr(self, user):
        if hasattr(user, 'uvt_user'):
            return user.uvt_user.ANR
        else:
            return ''

    def full_name(self, user):
        if hasattr(user, 'uvt_user'):
            return user.uvt_user.full_name
        else:
            return ''

# Re-register UserAdmin
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
