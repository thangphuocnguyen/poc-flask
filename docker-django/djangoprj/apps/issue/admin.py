from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):

    ordering = ['title']

admin.site.register(Issue, IssueAdmin)
