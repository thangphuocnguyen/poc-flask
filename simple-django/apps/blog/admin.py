from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'publish',
        'status',
        'user'
    )

    list_filter = ('status', 'created', 'publish', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # # raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ['status', '-publish', 'user']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('body',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
