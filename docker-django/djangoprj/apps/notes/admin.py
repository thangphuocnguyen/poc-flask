from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'pub_date',
        'title',
        'slug',
        'body'
    )

    # list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']

admin.site.register(Note, NoteAdmin)
