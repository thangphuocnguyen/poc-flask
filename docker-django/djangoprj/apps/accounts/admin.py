# from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
# Unregister Groups model which is not used
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')
    list_display_links = ('email',)

    search_fields = ('email',)
    list_filter = ('is_active', 'is_superuser', 'is_staff')

admin.site.register(User, UserAdmin)
